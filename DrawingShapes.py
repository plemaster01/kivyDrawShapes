from kivy.app import App
from kivy.graphics import Color, Rectangle, Ellipse, Line
from kivy.uix.widget import Widget


class MainWidget(Widget):
    rect = None
    circle = None
    line = None

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_shapes()

    def init_shapes(self):
        with self.canvas:
            Color(1, 0, 0)
            self.rect = Rectangle(bg_color=Color(1, 1, 0))
            self.circle = Ellipse(bg_color=Color(1, 0, 0))
            self.line = Line(bg_color=Color(1, 0, 1))

    def on_size(self, *args):
        print(self.size)
        self.rect.pos = (0, 0)
        self.rect.size = (int(self.width / 2), int(self.height))
        self.circle.pos = (int(self.width / 2), int(self.height * 3 / 4))
        self.circle.size = (int(self.width / 4), int(self.height / 4))
        self.line.points = (0, 0, int(self.width), int(self.height))
        self.line.width = 5


class MyApp(App):
    pass


if __name__ == '__main__':
    MyApp().run()
