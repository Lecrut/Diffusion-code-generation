class RightAngledTriangle:
    def __init__(self, height):
        self.height = height
        self.triangle = [[0] * (i + 1) for i in range(height)]

    def generate_triangle(self):
        for i in range(self.height):
            for j in range(i + 1):
                self.triangle[i][j] = 1

    def print_triangle(self):
        for row in self.triangle:
            print(row)

if __name__ == '__main__':
    triangle = RightAngledTriangle(5)
    triangle.generate_triangle()
    triangle.print_triangle()