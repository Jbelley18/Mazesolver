from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)
        canvas.pack()

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("My Window")

        # Create and pack the canvas
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()

        # Data member to track the "running" state of the window
        self.running = False

        # Set the method to call when the window is closed
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        # Redraw the window
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        # Run the window until it's closed
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        # Close the window
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
