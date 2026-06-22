def print_pyramid(height):
    if height <= 0:
        return
    else:
        print('*' * (2 * height - 1))
        print_pyramid(height - 1)

if __name__ == '__main__':
    height = 4
    print_pyramid(height)