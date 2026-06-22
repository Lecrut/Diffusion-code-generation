def generate_centered_triangle(n):
    return [' ' * (n - i) + '* ' * i + ' ' * (n - i) for i in range(1, n + 1)]
if __name__ == '__main__':
    levels = 12
    triangle = generate_centered_triangle(levels)
    print('\n'.join(triangle))