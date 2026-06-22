def print_pyramid(height, current_height=1):
    if height == 0:
        return
    spaces = ' ' * (height - current_height)
    stars = '*' * (2 * current_height - 1)
    print(spaces + stars)
    print_pyramid(height, current_height + 1)

if __name__ == '__main__':
    pyramid_height = 6
    print_pyramid(pyramid_height)