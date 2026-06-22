def generate_triangle(base):
    return '\n'.join(['*' * i for i in range(1, base + 1)])

if __name__ == '__main__':
    print(generate_triangle(10))