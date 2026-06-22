def validate_dimensions(width, height):
    if not (isinstance(width, int) and isinstance(height, int)):
        raise ValueError("Width and height must be integers")
    if width < 1 or height < 1:
        raise ValueError("Width and height must be greater than zero")

def fill_rectangle(width, height, symbol):
    validate_dimensions(width, height)
    return [symbol * width for _ in range(height)]

if __name__ == '__main__':
    width = 10
    height = 5
    symbol = "*"
    rectangle = fill_rectangle(width, height, symbol)
    for row in rectangle:
        print(row)