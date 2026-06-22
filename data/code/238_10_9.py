def validate_dimensions(width, height):
    if not (isinstance(width, int) and isinstance(height, int)):
        raise ValueError("Width and height must be integers")
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive")

def print_box():
    width = 5
    height = 3
    validate_dimensions(width, height)
    for i in range(height):
        if i == 0 or i == height - 1:
            print('*' * width)
        else:
            print('*' + ' ' * (width - 2) + '*')

if __name__ == '__main__':
    print_box()