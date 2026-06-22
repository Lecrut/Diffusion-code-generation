import math

def square_properties(area):
    side_length = math.sqrt(area)
    perimeter = 4 * side_length
    return side_length, perimeter

if __name__ == '__main__':
    area = 16
    side_length, perimeter = square_properties(area)
    print(f"Side Length: {side_length}, Perimeter: {perimeter}")