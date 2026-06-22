import turtle

class TriangleDrawer:
    side_length = 100

    @staticmethod
    def calculate_vertices():
        angle_step = 2 * math.pi / 3
        vertices = []
        for i in range(3):
            angle = i * angle_step
            x = TriangleDrawer.side_length * math.cos(angle)
            y = TriangleDrawer.side_length * math.sin(angle)
            vertices.append((x, y))
        return vertices

    def draw_triangle(self):
        turtle.speed(1)
        vertices = self.calculate_vertices()
        for _ in range(3):
            turtle.penup()
            turtle.goto(vertices.pop())
            turtle.pendown()
            turtle.forward(self.side_length)

if __name__ == '__main__':
    drawer = TriangleDrawer()
    drawer.draw_triangle()