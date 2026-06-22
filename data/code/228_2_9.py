import turtle

class EquilateralTriangleDrawer:
    SIDE_LENGTH = 100
    
    @staticmethod
    def calculate_coordinates():
        angle_step = 2 * 3.14159 / 3
        vertices = []
        for i in range(3):
            angle = i * angle_step
            x = EquilateralTriangleDrawer.SIDE_LENGTH * math.cos(angle)
            y = EquilateralTriangleDrawer.SIDE_LENGTH * math.sin(angle)
            vertices.append((x, y))
        return vertices
    
    def draw_triangle(self):
        vertices = self.calculate_coordinates()
        turtle.penup()
        turtle.goto(vertices[0])
        turtle.pendown()
        for vertex in vertices:
            turtle.goto(vertex)
        turtle.goto(vertices[0])

if __name__ == '__main__':
    drawer = EquilateralTriangleDrawer()
    drawer.draw_triangle()