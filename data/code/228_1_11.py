class RightAngledTriangle:
    def __init__(self, height):
        self.height = height
        self.triangle = [[0 for _ in range(i+1)] for i in range(height)]

    def generate_triangle(self):
        for i in range(self.height):
            for j in range(i+1):
                self.triangle[i][j] = 1

if __name__ == '__main__':
    triangle = RightAngledTriangle(5)
    triangle.generate_triangle()
    print(triangle.triangle)