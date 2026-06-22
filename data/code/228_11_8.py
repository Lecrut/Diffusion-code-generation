def generate_ascii_triangle(base_length):
    return '\n'.join([' ' * (base_length - i) + '*' * (2 * i - 1) for i in range(1, base_length + 1)])

if __name__ == '__main__':
    print(generate_ascii_triangle(10))