def validate_dimensions(width, height):
    if not isinstance(width, int) or width <= 0:
        raise ValueError("Width must be a positive integer")
    if not isinstance(height, int) or height <= 0:
        raise ValueError("Height must be a positive integer")

def generate_rectangle(width, height, symbol):
    validate_dimensions(width, height)
    return [symbol * width for _ in range(height)]

if __name__ == '__main__':
    result = generate_rectangle(5, 3, '#')
    print(result)