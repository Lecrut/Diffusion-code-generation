class StarTriangle:
    def __init__(self, height):
        self.height = height

    def print_triangle(self):
        for i in range(1, self.height + 1):
            print('*' * i)

if __name__ == '__main__':
    triangle = StarTriangle(5)
    triangle.print_triangle()