def generate_triangle(base):
    triangle = []
    for i in range(1, base + 1):
        row = '*' * i
        triangle.append(row)
    return '\n'.join(triangle)

if __name__ == '__main__':
    sample_base = 7
    print(generate_triangle(sample_base))