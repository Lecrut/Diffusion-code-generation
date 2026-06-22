MAX_HEIGHT = 5

def generate_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)

if __name__ == '__main__':
    triangle_height = MAX_HEIGHT
    generate_triangle(triangle_height)