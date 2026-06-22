def generate_triangle(base):
    return '\n'.join([' ' * (base - i - 1) + '*' * (2 * i + 1) for i in range(base)])

if __name__ == '__main__':
    print(generate_triangle(10))