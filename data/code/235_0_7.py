def generate_right_angled_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)

if __name__ == '__main__':
    triangle_height = 5
    generate_right_angled_triangle(triangle_height)