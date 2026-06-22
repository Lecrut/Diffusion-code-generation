def generate_right_triangle(n):
    return '\n'.join(['*' * (i + 1) for i in range(n)])

if __name__ == '__main__':
    print(generate_right_triangle(5))