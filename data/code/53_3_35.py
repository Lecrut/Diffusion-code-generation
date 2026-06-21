import math

def find_side_length(area):
    if not isinstance(area, (int, float)):
        raise TypeError("Area must be a number")
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

if __name__ == '__main__':
    sample_area = 64.0
    try:
        side_length = find_side_length(sample_area)
        print(f"The side length of the square is: {side_length}")
    except Exception as e:
        print(e)