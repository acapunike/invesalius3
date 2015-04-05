#--------------------------------------------------------------------------
# Software:     InVesalius - Software de Reconstrucao 3D de Imagens Medicas
# Copyright:    (C) 2001  Centro de Pesquisas Renato Archer
# Homepage:     http://www.softwarepublico.gov.br
# Contact:      invesalius@cti.gov.br
# License:      GNU - GPL 2 (LICENSE.txt/LICENCA.txt)
#--------------------------------------------------------------------------
#    Este programa e software livre; voce pode redistribui-lo e/ou
#    modifica-lo sob os termos da Licenca Publica Geral GNU, conforme
#    publicada pela Free Software Foundation; de acordo com a versao 2
#    da Licenca.
#
#    Este programa eh distribuido na expectativa de ser util, mas SEM
#    QUALQUER GARANTIA; sem mesmo a garantia implicita de
#    COMERCIALIZACAO ou de ADEQUACAO A QUALQUER PROPOSITO EM
#    PARTICULAR. Consulte a Licenca Publica Geral GNU para obter mais
#    detalhes.
#--------------------------------------------------------------------------

import wx
import vtk
from vtk.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor
import wx.lib.agw.floatspin as FS

class RegistrationDialog(wx.Dialog):
    def __init__(self, parent, title):
        wx.Dialog.__init__(self, parent)
        self.build_gui()
        self.build_source()
        
    def build_gui(self):
        # Panels
        self.pn1 = wx.Panel(self, -1)
        self.pn2 = wx.Panel(self, -1)
        self.pn1.SetBackgroundColour('LIGHT GRAY')
        self.pn2.SetBackgroundColour('LIGHT GRAY')
        
        # SECTION 1: TRANSLATE SOURCE TOOLS
        self.txt1 = "GEOMETRIC TRANSFORMATIONS"
        sb1 = wx.StaticBox(self.pn2, -1, self.txt1)
        self.alpha = wx.StaticText(self.pn2, -1, 'X', (-1, -1))
        self.beta = wx.StaticText(self.pn2, -1, 'Y', (-1, -1))
        self.gamma = wx.StaticText(self.pn2, -1, 'Z', (-1, -1))
        self.xrot = wx.StaticText(self.pn2, -1, 'Rot X', (-1, -1))
        self.yrot = wx.StaticText(self.pn2, -1, 'Rot Y', (-1, -1))
        self.zrot = wx.StaticText(self.pn2, -1, 'Rot Z', (-1, -1))
        self.angle = wx.StaticText(self.pn2, -1, 'Angle (W)', (-1, -1))
        line1H1 = wx.StaticLine(self.pn2, -1, style=wx.LI_HORIZONTAL)
        line1H2 = wx.StaticLine(self.pn2, -1, style=wx.LI_HORIZONTAL)
        self.brs = wx.Button(self.pn2, wx.ID_ANY, "Reset source", (-1, -1), (-1, -1))
        self.bincr = wx.Button(self.pn2, wx.ID_ANY, "Change increment value",
                               (-1, -1), (-1, -1))
        self.brsps = wx.Button(self.pn2, wx.ID_ANY, 'Reset spinbuttons', (-1, -1), (-1, -1)) 
        self.sp_1a = FS.FloatSpin(self.pn2, wx.ID_ANY, pos=(-1, -1), size=(-1, -1),
                                  style=FS.FS_CENTRE, value=0, min_val=-360,
                                  max_val=360, increment=1, digits=0)     
        self.sp_1b = FS.FloatSpin(self.pn2, wx.ID_ANY, pos=(-1, -1), size=(-1, -1),
                                  style=FS.FS_CENTRE, value=0, min_val=-360,
                                  max_val=360, increment=1, digits=0) 
        self.sp_1c = FS.FloatSpin(self.pn2, wx.ID_ANY, pos=(-1, -1), size=(-1, -1),
                                  style=FS.FS_CENTRE, value=0, min_val=-360,
                                  max_val=360, increment=1, digits=0)
        self.sp_1d = FS.FloatSpin(self.pn2, wx.ID_ANY, pos=(-1, -1), size=(-1, -1),
                                  style=FS.FS_CENTRE, value=0, min_val=-360,
                                  max_val=360, increment=1, digits=0)
        self.sp_1ax = FS.FloatSpin(self.pn2, wx.ID_ANY, pos=(-1, -1), size=(-1, -1),
                                   style=FS.FS_CENTRE, value=0, min_val=-360,
                                   max_val=360, increment=1, digits=0)     
        self.sp_1by = FS.FloatSpin(self.pn2, wx.ID_ANY, pos=(-1, -1), size=(-1, -1),
                                   style=FS.FS_CENTRE, value=0, min_val=-360,
                                   max_val=360, increment=1, digits=0) 
        self.sp_1cz = FS.FloatSpin(self.pn2, wx.ID_ANY, pos=(-1, -1), size=(-1, -1),
                                   style=FS.FS_CENTRE, value=0, min_val=-360,
                                   max_val=360, increment=1, digits=0)
        self.sp_3 = FS.FloatSpin(self.pn2, wx.ID_ANY, pos=(-1, -1), size=(-1, -1),
                                 style=FS.FS_CENTRE, value=0, min_val=1,
                                 max_val=100, increment=1, digits=0)
        
        # SECTION 1: Sizers
        t1_H = wx.BoxSizer(wx.HORIZONTAL)
        t2_H = wx.BoxSizer(wx.HORIZONTAL)
        t3_H = wx.BoxSizer(wx.HORIZONTAL)
        t4_H = wx.BoxSizer(wx.HORIZONTAL)
        t5_H = wx.BoxSizer(wx.HORIZONTAL)
        sbsz1_V = wx.StaticBoxSizer(sb1, wx.VERTICAL)
        
        # SECTION 2: SOURCE PROPERTIES
        self.txt2 = "PROPERTIES"
        sb2 = wx.StaticBox(self.pn2, -1, self.txt2)
        self.x = wx.StaticText(self.pn2, -1, '  R  ', (-1, -1))
        self.y = wx.StaticText(self.pn2, -1, '  G  ', (-1, -1))
        self.z = wx.StaticText(self.pn2, -1, '  B  ', (-1, -1)) 
        self.d = wx.StaticText(self.pn2, -1, '  Diameter  ', (-1, -1))
        self.h = wx.StaticText(self.pn2, -1, '  Height  ', (-1, -1))
        self.bexit = wx.Button(self.pn2, wx.ID_ANY, 'EXIT', (-1, -1), (-1, -1))
        self.sp_2a = FS.FloatSpin(self.pn2, wx.ID_ANY, pos=(-1, -1), size=(-1, -1),
                                 style=FS.FS_CENTRE, value=0, min_val=-360,
                                 max_val=360, increment=1, digits=0)     
        self.sp_2b = FS.FloatSpin(self.pn2, wx.ID_ANY, pos=(-1, -1), size=(-1, -1),
                                  style=FS.FS_CENTRE, value=0, min_val=-360,
                                  max_val=360, increment=1, digits=0) 
        self.sp_2c = FS.FloatSpin(self.pn2, wx.ID_ANY, pos=(-1, -1), size=(-1, -1),
                                  style=FS.FS_CENTRE, value=0, min_val=-360,
                                  max_val=360, increment=1, digits=0)
        self.sp_2d = FS.FloatSpin(self.pn2, wx.ID_ANY, pos=(-1, -1), size=(-1, -1),
                                  style=FS.FS_CENTRE, value=0, min_val=0,
                                  max_val=360, increment=1, digits=0)
        self.sp_2e = FS.FloatSpin(self.pn2, wx.ID_ANY, pos=(-1, -1), size=(-1, -1),
                                  style=FS.FS_CENTRE, value=0, min_val=0,
                                  max_val=360, increment=1, digits=0)
        
        # SECTION 2: Sizers
        s1_H = wx.BoxSizer(wx.HORIZONTAL)
        s2_H = wx.BoxSizer(wx.HORIZONTAL)
        s3_H = wx.BoxSizer(wx.HORIZONTAL)
        s4_H = wx.BoxSizer(wx.HORIZONTAL)
        s5_H = wx.BoxSizer(wx.HORIZONTAL)
        sbsz2_V = wx.StaticBoxSizer(sb2, wx.VERTICAL)
        
        # Changing the font of the texts on the GUI
        font_style = wx.Font(10, wx.FONTFAMILY_SWISS, wx.NORMAL, wx.BOLD)
        self.alpha.SetFont(font_style)
        self.beta.SetFont(font_style)
        self.gamma.SetFont(font_style)
        self.angle.SetFont(font_style)
        self.xrot.SetFont(font_style)
        self.yrot.SetFont(font_style)
        self.zrot.SetFont(font_style)
        self.x.SetFont(font_style)
        self.y.SetFont(font_style)
        self.z.SetFont(font_style)
        self.d.SetFont(font_style)
        self.h.SetFont(font_style)
        
        # LAYOUT CONSTRUCTION
        t1_H.Add(self.alpha, 0, wx.ALL | wx.EXPAND, 5)
        t1_H.Add(self.sp_1a, 1, wx.ALL | wx.EXPAND, 5)
        t1_H.Add(self.xrot, 0, wx.ALL | wx.EXPAND, 5)
        t1_H.Add(self.sp_1ax, 1, wx.ALL | wx.EXPAND, 5)
        t2_H.Add(self.beta, 0, wx.ALL | wx.EXPAND, 5)
        t2_H.Add(self.sp_1b, 1 , wx.ALL | wx.EXPAND, 5)
        t2_H.Add(self.yrot, 0, wx.ALL | wx.EXPAND, 5)
        t2_H.Add(self.sp_1by, 1, wx.ALL | wx.EXPAND, 5)
        t3_H.Add(self.gamma, 0, wx.ALL | wx.EXPAND, 5)
        t3_H.Add(self.sp_1c, 1, wx.ALL | wx.EXPAND, 5)
        t3_H.Add(self.zrot, 0, wx.ALL | wx.EXPAND, 5)
        t3_H.Add(self.sp_1cz, 1, wx.ALL | wx.EXPAND, 5)
        t4_H.Add(self.angle, 1, wx.ALL | wx.EXPAND, 5)
        t4_H.Add(self.sp_1d, 3, wx.ALL | wx.EXPAND, 5)
        t5_H.Add(self.bincr, 1, wx.ALL | wx.EXPAND, 5)
        t5_H.Add(self.sp_3, 1, wx.ALL | wx.EXPAND, 5)
        
        sbsz1_V.Add(t1_H, 1, wx.ALL | wx.EXPAND, 2)
        sbsz1_V.Add(t2_H, 1, wx.ALL | wx.EXPAND, 2)
        sbsz1_V.Add(t3_H, 1, wx.ALL | wx.EXPAND, 2)
        sbsz1_V.Add(t4_H, 1, wx.ALL | wx.EXPAND, 2)
        sbsz1_V.Add(self.brs, 1, wx.ALL | wx.EXPAND, 3)
        sbsz1_V.Add(line1H1, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER, 1)
        sbsz1_V.Add(t5_H, 1, wx.ALL | wx.EXPAND, 1)
        sbsz1_V.Add(line1H2, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER, 1)
        sbsz1_V.Add(self.brsps, 1, wx.ALL | wx.EXPAND, 3)
                
        s1_H.Add(self.x, 0, wx.ALL | wx.EXPAND, 5)
        s1_H.Add(self.sp_2a, 1, wx.ALL | wx.EXPAND, 5)
        s2_H.Add(self.y, 0, wx.ALL | wx.EXPAND, 5)
        s2_H.Add(self.sp_2b, 1, wx.ALL | wx.EXPAND, 5)
        s3_H.Add(self.z, 0, wx.ALL | wx.EXPAND, 5)
        s3_H.Add(self.sp_2c, 1, wx.ALL | wx.EXPAND, 5)
        s4_H.Add(self.d, 1, wx.ALL | wx.EXPAND, 5)
        s4_H.Add(self.sp_2d, 2, wx.ALL | wx.EXPAND, 5)
        s5_H.Add(self.h, 1, wx.ALL | wx.EXPAND, 5)
        s5_H.Add(self.sp_2e, 2, wx.ALL | wx.EXPAND, 5)
        
        sbsz2_V.Add(s1_H, 1, wx.ALL | wx.EXPAND, 3)
        sbsz2_V.Add(s2_H, 1, wx.ALL | wx.EXPAND, 3)
        sbsz2_V.Add(s3_H, 1, wx.ALL | wx.EXPAND, 3)
        sbsz2_V.Add(s4_H, 1, wx.ALL | wx.EXPAND, 3)
        sbsz2_V.Add(s5_H, 1, wx.ALL | wx.EXPAND, 3)
        sbsz2_V.Add(self.bexit, 1, wx.ALL | wx.EXPAND, 3) 

        sub_H = wx.BoxSizer(wx.HORIZONTAL)
        sub_H.Add(sbsz1_V, 1, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER, 5)
        line1V = wx.StaticLine(self.pn2, -1, style=wx.LI_VERTICAL)
        sub_H.Add(line1V, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER, 15)
        sub_H.Add(sbsz2_V, 1, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER, 5)
        self.pn2.SetSizer(sub_H)
        
        
        main_V = wx.BoxSizer(wx.VERTICAL)
        main_V.Add(self.pn1, 3, wx.EXPAND, 5)
        main_V.Add((wx.StaticLine(self.pn2, -1, style=wx.LI_HORIZONTAL)), 0, wx.EXPAND, 1)
        main_V.Add(self.pn2, 2, wx.EXPAND, 5)
        
        self.SetSizer(main_V)
        main_V.Fit(self)
        main_V.SetSizeHints(self)
        self.CentreOnScreen()
        
        # EVENTS        
        self.Bind(wx.EVT_SPINCTRL, self.OnTranslateRotate, self.sp_1ax)
        self.Bind(wx.EVT_SPINCTRL, self.OnTranslateRotate, self.sp_1by)
        self.Bind(wx.EVT_SPINCTRL, self.OnTranslateRotate, self.sp_1cz)
        self.Bind(wx.EVT_SPINCTRL, self.OnTranslateRotate, self.sp_1a)
        self.Bind(wx.EVT_SPINCTRL, self.OnTranslateRotate, self.sp_1b)
        self.Bind(wx.EVT_SPINCTRL, self.OnTranslateRotate, self.sp_1c)
        self.Bind(wx.EVT_SPINCTRL, self.OnTranslateRotate, self.sp_1d)
        
        self.Bind(wx.EVT_SPINCTRL, self.OnColour, self.sp_2a)
        self.Bind(wx.EVT_SPINCTRL, self.OnColour, self.sp_2b)
        self.Bind(wx.EVT_SPINCTRL, self.OnColour, self.sp_2c)
        self.Bind(wx.EVT_SPINCTRL, self.OnDiameter, self.sp_2d)
        self.Bind(wx.EVT_SPINCTRL, self.OnHeight, self.sp_2e)
        
        self.Bind(wx.EVT_BUTTON, self.OnDefault, self.brs)
        self.Bind(wx.EVT_BUTTON, self.OnChangeIncr, self.bincr) 
        self.Bind(wx.EVT_BUTTON, self.OnClear, self.brsps)    
        self.Bind(wx.EVT_BUTTON, self.OnShutDown, self.bexit)
        
    def build_source(self):
        # create source
        self.source = vtk.vtkCylinderSource()
        self.position = self.source.SetCenter(0, 0, 0)
        self.source.SetRadius(1.25)
        self.source.SetHeight(7.50)
        self.source.SetResolution(5)
         
        # mapper
        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInput(self.source.GetOutput())
 
        # actor
        self.actor = vtk.vtkActor()
        self.actor.SetMapper(self.mapper)
        self.actor.SetPosition(0, 0, 0)
        self.col = self.actor.GetProperty().SetColor(1.0 , 2.0, 2.5)
        self.pos = self.actor.GetPosition()
        
        axes = vtk.vtkAxesActor()
        axes.SetXAxisLabelText('x')
        axes.SetYAxisLabelText('y')
        axes.SetZAxisLabelText('z')
        axes.SetTotalLength(5, 5, 5)
   
        
        ren = vtk.vtkRenderer() 
        ren.AddActor(self.actor)
        ren.AddActor(axes)
        
        render_window = vtk.vtkRenderWindow()
        render_window.AddRenderer(ren)

        self.irenwin = wxVTKRenderWindowInteractor(self.pn1, -1,
                                                  size=self.pn1.GetSize())
        self.irenwin.SetRenderWindow(render_window)
        self.irenwin.Show(1)
        self.irenwin.Render()
        
        pn1szr = wx.BoxSizer(wx.HORIZONTAL)
        pn1szr.Add(self.irenwin, 1, wx.EXPAND, 5)
        self.pn1.SetSizer(pn1szr)
        
    # EVENT FUNCTIONS    
    def OnTranslateRotate(self, event):
        a = spin_act(self.sp_1a) 
        b = spin_act(self.sp_1b) 
        c = spin_act(self.sp_1c)
        
        if a is None:
            a = 0.0
            
        if b is None:
            b = 0.0
            
        if c is None:
            c = 0.0
        
        x = spin_act(self.sp_1ax) 
        y = spin_act(self.sp_1by) 
        z = spin_act(self.sp_1cz)
        d = spin_act(self.sp_1d)
        
        if x is None:
            x = 0.0
            
        if y is None:
            y = 0.0
              
        if z is None:
            z = 0.0
            
        if d is None:
            d = 0.0
            
        transform_protocol(self)
        self.transform.Translate(float(a), float(b), float(c)) 
        self.transform.RotateX(x)
        self.transform.RotateY(y)
        self.transform.RotateZ(z)
        self.transform.RotateWXYZ(float(d), float(a), float(b), float(c))
        
    def OnColour (self, event): 
        r = spin_act(self.sp_2a) 
        g = spin_act(self.sp_2b) 
        b = spin_act(self.sp_2c)
        if r is None:
            r = 0.0
            
        if g is None:
            g = 0.0
            
        if b is None:
            b = 0.0 
        self.actor.GetProperty().SetColor(float(r), float(g), float(b))
        self.irenwin.Refresh()        
         
    def OnDiameter (self, event):
        spin_act(self.sp_2d) 
        diam = self.sp_2d.GetValue()
        radius = round(((diam) / 2), 0)
        self.source.SetRadius(radius)
        self.source.Update()
        self.irenwin.Refresh()
        
    def OnHeight (self, event):
        spin_act(self.sp_2e) 
        height = self.sp_2e.GetValue()
        self.source.SetHeight(height)
        self.source.Update()
        self.irenwin.Refresh() 
        
    def OnDefault(self, event):
        transform_protocol(self)
        self.transform.Translate(0,0,0) 
        self.transform.RotateX(0)
        self.transform.RotateY(0)
        self.transform.RotateZ(0)
        self.source.SetRadius(1.250)
        self.source.SetHeight(7.5)
        self.source.SetResolution(5)
        self.actor.GetProperty().SetColor(1.0 , 2.0, 2.5)
        self.source.Update()
        self.irenwin.Refresh() 
        print"\nSource object restored"    
                    
    def OnChangeIncr(self, event):
        val = self.sp_3.GetValue()
        change_incr(self, self.sp_1a, self.sp_1b, self.sp_1c, self.sp_1ax,
                         self.sp_1by, self.sp_1cz, self.sp_1d, self.sp_2a,
                         self.sp_2b, self.sp_2c, self.sp_2d, self.sp_2e, self.sp_3, val)
        print "\nNew increment value = %d" % val
            
    def OnClear(self, event):
        self.sp_1a.SetValue(0.0)
        self.sp_1b.SetValue(0.0)
        self.sp_1c.SetValue(0.0)
        self.sp_1d.SetValue(0.0)        
        self.sp_1ax.SetValue(0.0)
        self.sp_1by.SetValue(0.0)
        self.sp_1cz.SetValue(0.0)
        self.sp_2a.SetValue(0.0)
        self.sp_2b.SetValue(0.0)
        self.sp_2c.SetValue(0.0)
        self.sp_2d.SetValue(0.0)
        self.sp_2e.SetValue(0.0)
        self.sp_3.SetValue(0.0)
        print "\nAll spinbuttons are cleared" 
        
    def OnShutDown(self, event):
        self.Destroy()

# External Functions            
def change_incr(self, sp_1, sp_2, sp_3, sp_4, sp_5, sp_6, sp_7, sp_8, sp_9,
                  sp_10, sp_11, sp_12, sp_13, v):
    sp_1.SetIncrement(v)
    sp_2.SetIncrement(v)
    sp_3.SetIncrement(v)
    sp_4.SetIncrement(v)
    sp_5.SetIncrement(v)
    sp_6.SetIncrement(v) 
    sp_7.SetIncrement(v)
    sp_8.SetIncrement(v)
    sp_9.SetIncrement(v) 
    sp_10.SetIncrement(v)     

def spin_act(spinbut):
        value = 0.0
        delta = spinbut.GetValue() - value
        value = spinbut.GetValue()
        if delta > 0.0 or delta < 0.0:
            return value
        else:
            return 
        
def transform_protocol(self):
        self.transform = vtk.vtkTransform() 
        self.transformFilter = vtk.vtkTransformPolyDataFilter()
        self.transformFilter.SetTransform(self.transform)
        self.transformFilter.SetInputConnection(self.source.GetOutputPort())
        self.transformFilter.Update()        
        self.mapper.SetInput(self.transformFilter.GetOutput()) 
        self.irenwin.Refresh()
    
app = wx.App(False)
reg_dialog = RegistrationDialog(None, 'InVesalius 3 - Calibration' )
reg_dialog.ShowModal()
app.MainLoop()          
