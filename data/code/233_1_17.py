def validate_dimensions(width, height):
    if not (isinstance(width, int) and isinstance(height, int)):
        raise ValueError("Width and height must be integers.")
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers.")

def generate_rectangle(width, height, symbol='#'):
    validate_dimensions(width, height)
    return [symbol * width for _ in range(height)]

if __name__ == '__main__':
    rectangle = generate_rectangle(5, 3)
    print(rectangle)