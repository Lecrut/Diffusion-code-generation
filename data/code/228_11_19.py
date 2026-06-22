def generate_triangle(base):
    return '\n'.join('*' * (i + 1) for i in range(base))

if __name__ == '__main__':
    print(generate_triangle(10))