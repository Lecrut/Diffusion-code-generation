class StarTriangle:
    def __init__(self, rows):
        self.rows = rows

    def print_triangle(self):
        triangle_pattern = '\n'.join(['*' * i for i in range(1, self.rows + 1)])
        return triangle_pattern

if __name__ == '__main__':
    triangle = StarTriangle(5)
    print(triangle.print_triangle())