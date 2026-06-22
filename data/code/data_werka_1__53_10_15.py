import math

def calculate_side_length(area):
    return math.sqrt(area)

if __name__ == '__main__':
    area1 = 25.0
    side_length1 = calculate_side_length(area1)
    print(f"The side length of the square with area {area1} is: {side_length1}")

    area2 = 64.0
    side_length2 = calculate_side_length(area2)
    print(f"The side length of the square with area {area2} is: {side_length2}")