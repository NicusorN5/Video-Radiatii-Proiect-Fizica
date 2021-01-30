from manim import *
import math

#prima parte - intro + 
class Intro(Scene):
	def construct(self):
		title = Tex("Radiatii electromagnetice",font = 'Cambria Math')
		title.set_color(RED_C)

		self.play(ShowCreation(title))
		self.wait(2)

		title2 = Tex("Radiatii electromagnetice",font = 'Cambria Math')
		title2.to_corner(LEFT+UP)
		self.play(Transform(title,title2))

		#
		# list
		#
		grup1 = VGroup()

		p1 = Tex("1.) Definitie",font = 'Cambria Math')
		p1.set_color(YELLOW_C)
		self.play(ShowCreation(p1))
		self.wait(1)
		p1_m = Tex("1.) Definitie",font = 'Cambria Math')
		p1_m.to_corner(LEFT+UP)
		p1_m.scale(0.5)
		p1_m.shift(DOWN*0.5)
		
		grup1.add(p1_m)
		grup1.arrange(DOWN, center=False, aligned_edge=LEFT)
		self.play(Transform(p1,p1_m))

		p2 = Tex("2.) Modelul atomic folosit in exemple",font = 'Cambria Math')
		p2.set_color(YELLOW_C)
		self.play(ShowCreation(p2))
		self.wait(1)
		p2_m = Tex("2.) Modelul atomic folosit in exemple",font = 'Cambria Math')
		p2_m.to_corner(LEFT+UP)
		p2_m.scale(0.5)
		p2_m.shift(DOWN)

		grup1.add(p2_m)
		grup1.arrange(DOWN, center=False, aligned_edge=LEFT)
		self.play(Transform(p2,p2_m))

		p3 = Tex("3.) Lungimi de unda",font = 'Cambria Math')
		p3.set_color(YELLOW_C)
		self.play(ShowCreation(p3))
		self.wait(1)
		p3_m = Tex("3.) Lungimi de unda",font = 'Cambria Math')
		p3_m.to_corner(LEFT+UP)
		p3_m.scale(0.5)
		p3_m.shift(DOWN*1.5)

		grup1.add(p3_m)
		grup1.arrange(DOWN, center=False, aligned_edge=LEFT)
		self.play(Transform(p3,p3_m))

		p4 = Tex("4.) Radiatii ionizante",font = 'Cambria Math')
		p4.set_color(YELLOW_C)
		self.play(ShowCreation(p4))
		self.wait(1)
		p4_m = Tex("4.) Radiatii ionizante",font = 'Cambria Math')
		p4_m.to_corner(LEFT+UP)
		p4_m.scale(0.5)
		p4_m.shift(DOWN*2)

		grup1.add(p4_m)
		grup1.arrange(DOWN, center=False, aligned_edge=LEFT)
		self.play(Transform(p4,p4_m))

		p5 = Tex("5.) Perioada de injumatatire",font = 'Cambria Math')
		p5.set_color(YELLOW_C)
		self.play(ShowCreation(p5))
		self.wait(1)
		p5_m = Tex("5.) Perioada de injumatatire",font = 'Cambria Math')
		p5_m.to_corner(LEFT+UP)
		p5_m.scale(0.5)
		p5_m.shift(DOWN*2.5)
	
		grup1.add(p5_m)
		grup1.arrange(DOWN, center=False, aligned_edge=LEFT)
		self.play(Transform(p5,p5_m))

		p6 = Tex("6.) Poluare electomagnetica",font = 'Cambria Math')
		p6.set_color(YELLOW_C)
		self.play(ShowCreation(p6))
		self.wait(1)
		p6_m = Tex("6.) Poluare electromagnetica",font = 'Cambria Math')
		p6_m.to_corner(LEFT+UP)
		p6_m.scale(0.5)
		p6_m.shift(DOWN*2.5)
	
		grup1.add(p6_m)
		grup1.arrange(DOWN, center=False, aligned_edge=LEFT)
		self.play(Transform(p6,p6_m))

		self.wait(5)
		self.play(FadeOut(title),FadeOut(p1),FadeOut(p2),FadeOut(p3),FadeOut(p4),FadeOut(p5),FadeOut(p6))
		self.wait(1)

class Partea1(Scene):
	def construct(self):

		g1 = VGroup()

		txt1 = Tex("1.) Definitie",font = 'Cambria Math')
		txt1.set_color(RED_C)
		self.play(ShowCreation(txt1))

		txt2 = Tex("1.) Definitie",font = 'Cambria Math')
		txt2.set_color(YELLOW_C)
		txt2.to_corner(UP+LEFT)
		g1.add(txt2)
		g1.arrange(DOWN, center=False, aligned_edge=LEFT)
		self.play(Transform(txt1,txt2))

		txtdef = Tex("Radiația electromagnetică este o combinație de câmpuri electrice și magnetice oscilante care se propagă prin spațiu și care transportă energie dintr-un loc în altul.")
		txtdef.to_corner(UP+LEFT)
		txtdef.shift(DOWN*0.5)
		txtdef.scale(0.75)
		g1.add(txtdef)
		g1.arrange(DOWN, center=False, aligned_edge=LEFT)
		self.play(ShowCreation(txtdef))

		self.wait(10)
		self.play(FadeOut(txtdef))

		#Electron electric field
		grid = NumberPlane()
		txt3 = Tex("Aproximare a unui camp vectorial generat de un electron")
		txt3.to_corner(UP+LEFT)
		txt3.set_color(YELLOW_C)
		txt3.add_background_rectangle()
		self.play(FadeOut(txt1),ShowCreation(grid))
		electron = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\electron.png")
		
		vf_electron = VectorField(self.electric_field_singular)
		self.play(ShowCreation(vf_electron),FadeIn(electron),ShowCreation(txt3))

		formula1 = Tex(r'$$ V_{f}(p(x,y)) = (cos(arctg2(y,x),sin(arctg2(y,x)))*\frac{q}{4\pi (|p|)^3} $$')
		formula1.to_corner(UP+LEFT)
		formula1.shift(DOWN*0.5)
		formula1.set_color_by_gradient("#33ccff","#ff00ff")
		formula1.add_background_rectangle()
		self.play(ShowCreation(formula1))
		self.wait(3)

		formula2 = Tex(r'$$ V_{f}(p(x,y)) = (|p|_{x},|p|_{y})*\frac{q}{4\pi (|p|)^3} $$')
		formula2.to_corner(UP+LEFT)
		formula2.shift(DOWN*0.5)
		formula2.set_color_by_gradient("#33ccff","#ff00ff")
		formula2.add_background_rectangle()
		self.play(Transform(formula1,formula2))
		self.wait(5)

		txt4 = Tex("Aproximare a unui camp vectorial generat de un magnet")
		txt4.to_corner(UP+LEFT)
		txt4.set_color(YELLOW_C)
		txt4.add_background_rectangle()
		self.play(FadeOut(vf_electron),FadeOut(electron),FadeOut(formula1))

		magnet = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\magnet.png")
		
		vf = VectorField(self.electric_field_calc,0.3,0.3,0,0.25)
		
		self.play(ShowCreation(vf),FadeIn(magnet),FadeOut(txt3))
		self.play(ShowCreation(txt4))

		self.wait(5)	

		self.play(FadeOut(txt4),FadeOut(vf),FadeOut(grid),FadeOut(magnet))
		self.wait(2)

	def electric_field_calc(self,p):
		r1 = self.electric_field_point(p,-0.5,[1,0])
		r2 = self.electric_field_point(p,0.5,[-1,0])
		
		x = p[0] - 1
		y = p[1]
		d1 = math.sqrt((x*x+y*y))

		x1 = p[0] + 1
		d2 = math.sqrt(x1*x1+y*y)

		raza = 1.5

		if(d1 < raza and d2 > raza):
			return r1
		if(d2 < raza and d1 > raza):
			return r2
		if(d1 < raza or d2 < raza):
			if(p[1] < 1.0 and p[1] > -1.0):
				if(p[0] > 0): return self.electric_field_point(p,-0.25,[0,0])
				if(p[0] < 0): return self.electric_field_point(p,0.25,[0,0])
			return [0.0,0.0]
		if(p[0] > 0): return r1
		return r2

	def electric_field_point(self,p,q,o):
		pi = 3.1415926
		x = p[0] - o[0]
		y = p[1] - o[1]
		r = math.sqrt(x*x+y*y)
		if(r == 0) :
			return [0.0,0.0]
		theta = math.atan2(y,x)
		rx = math.cos(theta)* (q/4*pi*r**3)
		ry = math.sin(theta)* (q/4*pi*r**3)
		return [rx,ry]

	def electric_field_singular(self,p):
		return self.electric_field_point(p,1,[0,0])

totaltime = 0.0

class Partea2(Scene):
	def construct(self):
		txt1 = Tex("2.) Modelul atomic folosit in exemple")
		txt1.set_color(RED_C)
		self.play(ShowCreation(txt1))
		self.wait(5)
		
		txt2 = Tex("2.) Modelul atomic folosit in exemple")
		txt2.to_corner(LEFT+UP)
		self.play(Transform(txt1,txt2))

		txt3 = Tex(r"Chiar daca modelul cuantic al atomului este cel mai apropiat de un adevar \newline absolut, pentru simplitate o sa folosim modelul Bohr.")
		txt3.scale(0.75)
		self.play(ShowCreation(txt3))
		self.wait(10)
		txt6 = Text("Functia unda a Hidrogenului in mecanica cuantica")
		txt6.to_corner(UP+LEFT)
		txt6.scale(0.5)
		txt6.shift(0.5*DOWN)
		txt7 = Text("Motivul pentru care evitam mecanica cuantica este natura ei aleatorie.")
		txt7.shift(DOWN)
		txt7.scale(0.5)

		txt4 = Tex(r"$$ \psi_{n \ell m}(r, \theta, \varphi) = \sqrt{{\left( \frac{2}{n a^*_0} \right)}^3 \frac{(n - \ell - 1)!}{2 n (n + \ell)!}} e^{-\rho / 2} \rho^{\ell} L_{n - \ell - 1}^{2 \ell + 1}(\rho) Y_\ell^m (\theta, \varphi)$$")
		txt4.scale(0.75)
		self.play(Transform(txt3,txt4),ShowCreation(txt6),ShowCreation(txt7))
		self.wait(4)
		self.play(FadeOut(txt3),FadeOut(txt1),FadeOut(txt6),FadeOut(txt7))

		hidrogen_model = ImageMobject(r"C:\Users\NicusorN5\Desktop\proiect fizica\IronPythonApplication1\media\assets\raster_images\Hydrogen_Density_Plots.png")
		#hidrogen_model.to_corner(UP+LEFT)
		hidrogen_model.scale(0.5)
		self.play(FadeIn(hidrogen_model))
		self.wait(10)
		self.play(FadeOut(hidrogen_model))

		electron1 = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\electron.png")
		electron1.shift(LEFT*2)
		electron2 = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\electron.png")
		electron2.shift(RIGHT*2)

		proton1 = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\proton.png")
		proton1.shift(DOWN*0.25+LEFT*0.25)
		proton2 = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\proton.png")
		proton2.shift(DOWN*-0.25+LEFT*-0.25)

		neutron1 = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\neutron.png")
		neutron1.shift((DOWN*0.25) + (LEFT*-0.25))
		neutron2 = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\neutron.png")
		neutron2.shift((-DOWN*0.25) + (LEFT*0.25))

		txt5 = Tex("Atomul de Heliu in modelul planetar")
		txt5.set_color(RED_C)
		txt5.to_edge(UP)
		self.play(FadeIn(electron1),FadeIn(electron2),FadeIn(proton1),FadeIn(proton2),FadeIn(neutron1),FadeIn(neutron2),FadeIn(txt5))
		
		electron1.add_updater(self.MoveElectronForward)
		electron2.add_updater(self.MoveElectronBackWard)

		self.wait(5)

		electron1.remove_updater(self.MoveElectronForward)
		electron2.remove_updater(self.MoveElectronBackWard)
		self.play(FadeOut(electron1),FadeOut(electron2),FadeOut(proton1),FadeOut(proton2),FadeOut(neutron1),FadeOut(neutron2),FadeOut(txt5))
		self.wait(5)

	def MoveElectronForward(self,e,dt):
		global totaltime
		totaltime += dt * 3
		e.move_to((RIGHT * math.cos(totaltime)*2) + (UP * math.sin(totaltime)*2))
		

	def MoveElectronBackWard(self,e,dt):
		global totaltime
		totaltime += dt * 3
		e.move_to((RIGHT * -math.cos(totaltime)*2) + (UP * -math.sin(totaltime)*2))

class Partea3(Scene):
	def construct(self):
		txt1 = Tex("3.) Lungimi de unda")
		txt1.set_color(RED_C)
		self.play(ShowCreation(txt1))

		txt2 = Tex("3.) Lungimi de unda")
		txt2.to_corner(UP+LEFT)
		self.play(Transform(txt1,txt2))
		self.wait(2)
		Img1 = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\EM_Spectrum.png")
		Img1.scale(2)
		self.play(FadeOut(txt1),FadeIn(Img1))
		self.wait(20)
		self.play(FadeOut(Img1))

		g1 = VGroup()
		txt3 = Tex("Ecuatiile unei singure unde electromagnetice sunt")
		txt3.to_corner(LEFT+UP)
		txt3.shift(DOWN*0.5)
		g1.add(txt3)

		txt4 = Tex(r"$$ \vec{E}(x,t) = E_{max}cos(kx - \omega t)\vec{j} $$")
		txt4.set_color_by_gradient(RED_C,YELLOW_C)
		g1.add(txt4)

		txt5 = Tex(r"$$ \vec{B}(x,t)=B_{max}cos(kx - \omega t)\vec{k} $$")
		txt5.set_color_by_gradient("#FF00FF",BLUE_C)
		g1.add(txt5)

		txt8 = Tex("cu propietatile:")
		g1.add(txt8)

		txt6 = Tex(r"$$ k = \frac{2 \pi}{\lambda} $$")
		txt6.set_color_by_gradient(RED_C,"#00ff00")
		g1.add(txt6)

		txt7 = Tex(r"$$ \omega = 2 \pi f $$")
		txt7.set_color_by_gradient("#ffff00","#0000ff")
		g1.add(txt7)

		txt9 = Tex("Obs: se foloseste varianta sinusoidala, nu ecuatiile lui Maxwell")
		g1.add(txt9)

		g1.arrange(DOWN,center = False,aligned_edge=LEFT)
		self.play(ShowCreation(txt3),ShowCreation(txt4),ShowCreation(txt5),ShowCreation(txt6),ShowCreation(txt7),ShowCreation(txt8),ShowCreation(txt9))
		self.wait(5)
		self.play(FadeOut(txt3),FadeOut(txt4),FadeOut(txt5),FadeOut(txt6),FadeOut(txt7),FadeOut(txt8),FadeOut(txt9))
		self.wait(1)

a = 1.0
b = 1.0
c = 0.0
d = 0.0
timer = 0.0

class GraficSinusoida(GraphScene):
	CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -4,
        "y_max": 4,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE
	}
	def construct(self):
		self.setup_axes(True)

		txt1 = Tex("Forma generala a unei sinusoide")
		txt1.set_color(RED_C)
		txt1.to_edge(UP)

		txt6 = Tex("$$ f(x) = a*sin(b*x+c)+d $$")
		txt6.set_color_by_gradient("#00FF00","FF0000")
		txt6.to_edge(UP)
		txt6.shift(DOWN)

		a = ValueTracker(1)
		b = ValueTracker(1)
		c = ValueTracker(0)
		d = ValueTracker(0)

		graph = self.get_graph(lambda x: a.get_value()*math.sin(x*b.get_value()+c.get_value())+d.get_value(),RED_C,-10,10)
		graph.add_updater(lambda m: m.become(self.get_graph(lambda x: a.get_value()*math.sin(x*b.get_value()+c.get_value())+d.get_value(),RED_C,-10,10)))
		
		txt2 = Tex('a = ')
		txt2.scale(0.5)
		txt2.to_corner(LEFT+UP)
		txt2.shift(DOWN*0.25)

		txt3 = Tex('b = ')
		txt3.scale(0.5)
		txt3.to_corner(LEFT+UP)
		txt3.shift(0.5*DOWN)

		txt4 = Tex('c = ')
		txt4.scale(0.5)
		txt4.to_corner(LEFT+UP)
		txt4.shift(0.75*DOWN)

		txt5 = Tex('d = ')
		txt5.scale(0.5)
		txt5.to_corner(LEFT+UP)
		txt5.shift(DOWN)

		g1 = VGroup(txt2,txt3,txt4,txt5)
		g1.arrange(DOWN,center=False, aligned_edge=LEFT)

		coef_a = DecimalNumber(0,3,True)
		coef_a.scale(0.5)

		coef_b = DecimalNumber(0,3,True)
		coef_b.scale(0.5)

		coef_c = DecimalNumber(0,3,True)
		coef_c.scale(0.5)

		coef_d = DecimalNumber(0,3,True)
		coef_d.scale(0.5)

		coef_a.move_to(txt2)
		coef_a.shift(RIGHT)

		coef_b.move_to(txt3)
		coef_b.shift(RIGHT)

		coef_c.move_to(txt4)
		coef_c.shift(RIGHT)

		coef_d.move_to(txt5)
		coef_d.shift(RIGHT)

		self.play(ShowCreation(graph),ShowCreation(txt1),ShowCreation(txt2),ShowCreation(txt3),ShowCreation(txt4),ShowCreation(txt5),ShowCreation(coef_a),ShowCreation(coef_b),ShowCreation(coef_c),ShowCreation(coef_d),ShowCreation(txt6))
		self.wait(2)

		self.play(ApplyMethod(a.increment_value,1),ChangeDecimalToValue(coef_a,1),run_time = 2)
		self.play(ApplyMethod(a.increment_value,-2),ChangeDecimalToValue(coef_a,-2),run_time = 4)
		self.play(ApplyMethod(a.increment_value,1),ChangeDecimalToValue(coef_a,1),run_time = 1)

		self.play(ApplyMethod(b.increment_value,1),ChangeDecimalToValue(coef_b,1),run_time = 2)
		self.play(ApplyMethod(b.increment_value,-2),ChangeDecimalToValue(coef_b,-2),run_time = 4)
		self.play(ApplyMethod(b.increment_value,1),ChangeDecimalToValue(coef_b,1),run_time = 1)

		self.play(ApplyMethod(c.increment_value,1),ChangeDecimalToValue(coef_c,1),run_time = 2)
		self.play(ApplyMethod(c.increment_value,-2),ChangeDecimalToValue(coef_c,-2),run_time = 4)
		self.play(ApplyMethod(c.increment_value,1),ChangeDecimalToValue(coef_c,1),run_time = 1)

		self.play(ApplyMethod(d.increment_value,1),ChangeDecimalToValue(coef_d,1),run_time = 2)
		self.play(ApplyMethod(d.increment_value,-2),ChangeDecimalToValue(coef_d,-2),run_time = 4)
		self.play(ApplyMethod(d.increment_value,1),ChangeDecimalToValue(coef_d,1),run_time = 1)

		self.play(FadeOut(graph),FadeOut(txt1),FadeOut(txt2),FadeOut(txt3),FadeOut(txt4),FadeOut(txt5),FadeOut(coef_a),FadeOut(coef_b),FadeOut(coef_c),FadeOut(coef_d),FadeOut(txt6))
		self.wait(2)

class Partea4(Scene):
	def construct(self):
		txt1 = Tex('4.) Radiatii ionizante')
		txt1.set_color(RED_C)
		self.play(ShowCreation(txt1))
		
		txt2 = Tex('4.) Radiatii ionizante')
		txt2.to_corner(UP+LEFT)
		self.play(Transform(txt1,txt2))
		
		g1 = VGroup()
		#g1.to_corner(LEFT+UP)
		#g1.shift(DOWN*2)
		txt3 = Tex("Def: Radiatiile sunt ionizante daca au destula energie sa dea afara un electron din orbita unui atom.")
		txt3.scale(0.8)
		txt3.to_corner(LEFT+UP)
		txt3.shift(DOWN*2)
		g1.add(txt3)
		g1.arrange(DOWN,center=False, aligned_edge=LEFT)

		self.play(ShowCreation(txt3))
		self.wait(7)
		self.play(FadeOut(txt3))

		electron1 = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\electron.png")
		electron1.shift(LEFT*2)
		electron2 = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\electron.png")
		electron2.shift(RIGHT*2)

		proton1 = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\proton.png")
		proton1.shift(DOWN*0.25+LEFT*0.25)
		proton2 = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\proton.png")
		proton2.shift(DOWN*-0.25+LEFT*-0.25)

		neutron1 = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\neutron.png")
		neutron1.shift((DOWN*0.25) + (LEFT*-0.25))
		neutron2 = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\neutron.png")
		neutron2.shift((-DOWN*0.25) + (LEFT*0.25))

		global totaltime
		totaltime = 0.0

		self.play(FadeIn(electron1),FadeIn(electron2),FadeIn(proton1),FadeIn(proton2),FadeIn(neutron1),FadeIn(neutron2))
		electron1.add_updater(self.MoveElectronForward)
		electron2.add_updater(self.MoveElectronBackWard)

		self.wait(5)

		proton3 = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\proton.png")
		proton3.shift(DOWN*5)

		proton4 = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\proton.png")
		proton4.move_to(DOWN*2)

		self.play(Transform(proton3,proton4))

		electron1.remove_updater(self.MoveElectronForward)
		electron4 = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\electron.png")
		electron4.move_to(DOWN*2+LEFT*0.25)
		self.remove(electron1)
		self.remove(proton3)
		self.add(electron4)

		proton5 = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\proton.png")
		proton5.move_to(UP*5+RIGHT*2)

		electron5 = ImageMobject("C:\\Users\\NicusorN5\\Desktop\\proiect fizica\\IronPythonApplication1\\media\\assets\\raster_images\\electron.png")
		electron5.move_to(DOWN*5+LEFT*2)
		self.play(Transform(electron4,electron5),Transform(proton4,proton5))
		self.wait(1)
		self.play(FadeOut(electron2),FadeOut(electron4),FadeOut(proton4),FadeOut(proton1),FadeOut(proton2),FadeOut(neutron1),FadeOut(neutron2))
		self.wait(1)

		g2 = VGroup()
		txt4 = Tex('Frecventa unui unde electromagnetice este:')
		txt4.to_corner(LEFT+UP)
		txt4.shift(DOWN)
		g2.add(txt4)

		txt5 = Tex(r'$$ \lambda = \frac{v}{f} $$')
		txt5.set_color_by_gradient(RED_C,YELLOW_C)
		g2.add(txt5)

		txt6 = Tex("Razele care pot ioniza atomii sunt cele cu frecvente")
		g2.add(txt6)

		txt7 = Tex(" mai mari sau egale ale razelor UV.")
		g2.add(txt7)

		g2.arrange(DOWN, center=False, aligned_edge=LEFT)
		
		self.play(ShowCreation(txt4),ShowCreation(txt5),ShowCreation(txt6),ShowCreation(txt7))
		self.wait(5)
		self.play(FadeOut(txt4),FadeOut(txt5),FadeOut(txt6),FadeOut(txt7),FadeOut(txt1))
		self.wait(1)

	def MoveElectronForward(self,e,dt):
		global totaltime
		totaltime += dt * 2
		e.move_to((RIGHT * math.cos(totaltime)*2) + (UP * math.sin(totaltime)*2))

	def MoveElectronBackWard(self,e,dt):
		global totaltime
		totaltime += dt * 2
		e.move_to((RIGHT * -math.cos(totaltime)*2) + (UP * -math.sin(totaltime)*2))
		
class Partea5(Scene):
	def construct(self):
		txt1 = Tex("5.) Perioada de injumatatire")
		txt1.set_color(RED_C)
		self.play(ShowCreation(txt1))

		txt2 = Tex("5.) Perioada de injumatatire")
		txt2.to_corner(LEFT+UP)
		self.play(Transform(txt1,txt2))

		g1 = VGroup()
		txt3 = Tex("Def: Perioada de înjumătățire este durata de timp necesară ")
		txt3.to_edge(UP+LEFT)
		txt3.shift(DOWN*2)
		g1.add(txt3)
		txt4 = Tex("pentru ca mărimea valorii unei cantități să scadă la ")
		txt5 = Tex("jumătate față de valoarea ei, măsurată la începutul perioadei.")
		g1.add(txt4)
		g1.add(txt5)
		g1.arrange(DOWN,center = False,aligned_edge = LEFT)
		self.play(ShowCreation(txt3),ShowCreation(txt4),ShowCreation(txt5))
		self.wait(5)
		
		self.play(FadeOut(txt1),FadeOut(txt3),FadeOut(txt4),FadeOut(txt5))
		self.wait(1)

class HalfLifeEquation(GraphScene):
	def half_life_example(self,x):
		return 5*math.exp(-0.5*x)
	def construct(self):
		self.setup_axes(True)
		graph = self.get_graph(self.half_life_example,"#00ff00",0,10)
		
		txt1 = Tex(r"$$ N(t) = N_{0} e^{- \lambda t} $$")
		txt1.set_color_by_gradient(RED_C,YELLOW_C)
		txt1.to_edge(UP)

		self.play(ShowCreation(graph),ShowCreation(txt1))
		self.wait(5)
		self.play(FadeOut(graph),FadeOut(txt1))
		self.wait(1)

class Partea6(Scene):
	def construct(self):
		txt1 = Tex("6.) Poluarea electromagnetica")
		txt1.set_color(RED_C)
		self.play(ShowCreation(txt1))
		
		txt2 = Tex("6.) Poluarea electromagnetica")
		txt2.to_corner(UP+LEFT)
		self.play(Transform(txt1,txt2))

		txt3 = Tex("Subiect de dezbatere :)")
		txt3.set_color_by_gradient(RED_C,YELLOW_C)
		self.play(ShowCreation(txt3))
		self.wait(20)
		self.play(FadeOut(txt1),FadeOut(txt3))
		self.wait(1)
