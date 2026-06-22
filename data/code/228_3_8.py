def generate_right_triangle(height):
    return '\n'.join(' '.join(str(i) for i in range(1, j + 1)) for j in range(1, height + 1))

if __name__ == '__main__':
    triangle_height = 7
    result = generate_right_triangle(triangle_height)
    print(result)