if __name__ == '__main__':
    rows = 6

    def validate_rows(rows):
        if not isinstance(rows, int) or rows <= 0:
            raise ValueError("Rows must be a positive integer")

    def print_inverted_right_triangle(rows):
        for i in range(rows, 0, -1):
            print('*' * i)

    validate_rows(rows)
    print_inverted_right_triangle(rows)