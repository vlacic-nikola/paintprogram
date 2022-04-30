from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Line, Color, Ellipse
import random 
from kivy.uix.button import Button


Window.clearcolor = (1,1,1,1)
class PaintWindow(Widget):
	def on_touch_down(self, touch):
		colorR = random.randint(0,255)
		colorB = random.randint(0,255)
		colorG = random.randint(0,255)
		self.canvas.add(Color(rgb = (colorR/255.0,colorB/255.0,colorG/255.0,1)))
		d = 30
		self.canvas.add(Ellipse(pos=(touch.x - d/2, touch.y - d/2), size = (d,d)))
		touch.ud['line'] = Line(points=(touch.x, touch.y))
		self.canvas.add(touch.ud['line'])
	def on_touch_move(self, touch):
		touch.ud['line'].points  += [touch.x, touch.y]
		


class PaintApp(App):
	def clear_canvas(self, obj):
		self.painter.canvas.clear()	
	def build(self):
		rootWindow = Widget()
		self.painter = PaintWindow()
		clearBtn = Button(text = 'Clear')
		clearBtn.bind(on_release=self.clear_canvas)
		rootWindow.add_widget(self.painter)
		rootWindow.add_widget(clearBtn)
		return rootWindow
		
	
PaintApp().run()

