class TrianglePattern:
    def print_triangle(self, rows):
        for i in range(1, rows + 1):
            print('*' * i)

if __name__ == '__main__':
    pattern = TrianglePattern()
    pattern.print_triangle(5)