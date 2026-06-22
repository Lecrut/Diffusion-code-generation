class StarTriangle:
    def __init__(self, rows):
        self.rows = rows

    def print_triangle(self):
        triangle_pattern = '\n'.join(['*' * i for i in range(1, self.rows + 1)])
        return triangle_pattern

if __name__ == '__main__':
    star_triangle_instance = StarTriangle(5)
    result = star_triangle_instance.print_triangle()
    print(result)