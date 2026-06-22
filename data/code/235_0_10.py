def create_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)

if __name__ == '__main__':
    triangle_height = 7
    create_triangle(triangle_height)