class StarTriangle:
    MAX_ROWS = 6

    @staticmethod
    def print_inverted_right_triangle(rows):
        if rows > StarTriangle.MAX_ROWS:
            raise ValueError("Rows must be less than or equal to 6")
        for i in range(rows, 0, -1):
            print('*' * i)

if __name__ == '__main__':
    triangle = StarTriangle()
    triangle.print_inverted_right_triangle(6)