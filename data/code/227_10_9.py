def print_star_triangle(rows):
    pattern = '\n'.join(['*' * i for i in range(1, rows + 1)])
    return pattern

if __name__ == '__main__':
    triangle_pattern = print_star_triangle(5)
    print(triangle_pattern)