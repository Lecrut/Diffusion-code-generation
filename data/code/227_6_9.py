def validate_height(height):
    if not isinstance(height, int) or height <= 0:
        raise ValueError("Height must be a positive integer")

def print_star_pyramid(height):
    validate_height(height)
    
    for i in range(1, height + 1):
        print(f"{' ' * (height - i)}*{' *' * (2 * i - 2)}*")

if __name__ == '__main__':
    try:
        print_star_pyramid(3)
    except ValueError as e:
        print(e)