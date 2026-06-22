def generate_right_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)

if __name__ == '__main__':
    generate_right_triangle(5)