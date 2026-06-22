def generate_centered_triangle(size):
    return [' ' * (size - i) + '*' * (2 * i - 1) for i in range(1, size + 1)]

if __name__ == '__main__':
    level = 12
    lines = generate_centered_triangle(level)
    print('\n'.join(lines))