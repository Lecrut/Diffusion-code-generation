import math

def calculate_perimeter(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Dimensions must be numeric")
    if width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive")
    return 2 * (width + height)

if __name__ == '__main__':
    width = 10
    height = 5
    result = calculate_perimeter(width, height)
    print(result)