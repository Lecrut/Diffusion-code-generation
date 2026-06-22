import math

def find_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

if __name__ == '__main__':
    sample_area = 49.0
    side_length = find_side_length(sample_area)
    print(side_length)