def print_inverted_right_triangle(rows):
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("Rows must be a positive integer")
    for i in range(rows, 0, -1):
        print('*' * i)

if __name__ == '__main__':
    try:
        print_inverted_right_triangle(6)
    except ValueError as e:
        print(e)