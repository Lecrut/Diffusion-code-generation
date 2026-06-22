if __name__ == '__main__':
    def print_right_angled_triangle(height):
        for i in range(1, height + 1):
            print('*' * i)

    height = 5
    if isinstance(height, int) and height > 0:
        print_right_angled_triangle(height)