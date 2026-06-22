def print_centered_triangle(levels):
    print('\n'.join(' ' * (levels - i - 1) + '*' * (2 * i + 1) for i in range(levels)))

if __name__ == '__main__':
    print_centered_triangle(12)