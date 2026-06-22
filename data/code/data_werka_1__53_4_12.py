import math

def find_side_length(area):
    side_length = math.sqrt(area)
    return side_length

if __name__ == '__main__':
    test_area = 49.0
    result = find_side_length(test_area)
    print(f"The side length of a square with area {test_area} is {result}")