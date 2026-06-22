import math

def calculate_square_side_and_perimeter(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    
    side_length = area ** 0.5
    perimeter = 4 * side_length
    
    return side_length, perimeter

if __name__ == '__main__':
    try:
        area_value = 16
        side_length, perimeter = calculate_square_side_and_perimeter(area_value)
        print(f"Side Length: {side_length}, Perimeter: {perimeter}")
    except ValueError as e:
        print(e)