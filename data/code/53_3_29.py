import math

def validate_area(area):
    if not isinstance(area, (int, float)):
        raise TypeError("Area must be a number")
    if area < 0:
        raise ValueError("Area cannot be negative")

def find_side_length(area):
    validate_area(area)
    return math.sqrt(area)

if __name__ == '__main__':
    sample_area = 64.0
    try:
        side_length = find_side_length(sample_area)
        print(side_length)
    except Exception as e:
        print(e)