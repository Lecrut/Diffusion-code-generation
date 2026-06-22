def generate_triangle(rows=20):
    return '\n'.join('*' * (i + 1) for i in range(rows))

if __name__ == '__main__':
    print(generate_triangle(20))