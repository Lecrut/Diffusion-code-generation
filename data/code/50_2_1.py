def print_centered_triangle(levels):
    triangle_lines = [' ' * (levels - i - 1) + '*' * (2 * i + 1) for i in range(levels)]
    return '\n'.join(triangle_lines)

if __name__ == '__main__':
    levels = 12
    result = print_centered_triangle(levels)
    print(result)