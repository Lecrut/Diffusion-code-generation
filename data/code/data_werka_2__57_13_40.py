def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers")
    return length * width

if __name__ == '__main__':
    DEFAULT_LENGTH = 8.5
    DEFAULT_WIDTH = 4.2
    area = calculate_area(DEFAULT_LENGTH, DEFAULT_WIDTH)
    print(area)