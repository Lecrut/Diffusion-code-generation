def construct_pyramid(height):
    if height <= 0:
        raise ValueError("Height must be greater than 0")
    
    def print_level(level, spaces, stars):
        print(' ' * spaces + '*' * stars)
    
    for i in range(height):
        spaces = height - i - 1
        stars = 2 * i + 1
        print_level(i, spaces, stars)

if __name__ == '__main__':
    construct_pyramid(5)