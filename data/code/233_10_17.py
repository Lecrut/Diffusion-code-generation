def validate_dimensions(width, height):
    if not (isinstance(width, int) and isinstance(height, int)):
        raise ValueError("Width and height must be integers")
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be greater than zero")

def create_rectangle_pattern(width, height, symbol):
    return "\n".join([symbol * width for _ in range(height)])

if __name__ == '__main__':
    width = 10
    height = 5
    symbol = "*"
    validate_dimensions(width, height)
    pattern = create_rectangle_pattern(width, height, symbol)
    print(pattern)