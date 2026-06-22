def generate_right_triangle(height):
    triangle = '\n'.join(' '.join(str(i) for i in range(1, j + 1)) for j in range(1, height + 1))
    return triangle

if __name__ == '__main__':
    print(generate_right_triangle(5))