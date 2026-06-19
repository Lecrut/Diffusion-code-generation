import math

def calculate_square_properties(area):
    side_length = math.sqrt(area)
    perimeter = 4 * side_length
    return {'side_length': side_length, 'perimeter': perimeter}

if __name__ == '__main__':
    area = 16
    properties = calculate_square_properties(area)
    print(f"Side Length: {properties['side_length']}, Perimeter: {properties['perimeter']}")