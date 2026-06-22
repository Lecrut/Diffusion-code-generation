if __name__ == '__main__':
    height = 5

    def print_triangle(height):
        for i in range(1, height + 1):
            print('*' * i)

    print_triangle(height)