def create_right_triangle(height):
    return '\n'.join(['* ' * i for i in range(1, height + 1)])

if __name__ == '__main__':
    print(create_right_triangle(5))