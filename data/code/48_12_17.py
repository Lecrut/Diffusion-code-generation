import math

def validate_area(area):
    if area <= 0:
        raise ValueError("Area must be a positive number")

def calculate_side_length(area):
    return math.sqrt(area)

def calculate_perimeter(side_length):
    return 4 * side_length

def square_properties(area):
    validate_area(area)
    side_length = calculate_side_length(area)
    perimeter = calculate_perimeter(side_length)
    return side_length, perimeter

if __name__ == '__main__':
    area = 16
    side_length, perimeter = square_properties(area)
    print(f"Side Length: {side_length}, Perimeter: {perimeter}")