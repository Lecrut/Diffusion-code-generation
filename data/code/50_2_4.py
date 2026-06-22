def create_centered_triangle(n):
    return '\n'.join([' ' * (n - i) + '*' * (2 * i - 1) for i in range(1, n + 1)])

if __name__ == '__main__':
    print(create_centered_triangle(12))