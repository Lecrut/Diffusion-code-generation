import math

def find_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    side_length = math.sqrt(area)
    return side_length

if __name__ == '__main__':
    sample_area = 36.0
    result = find_side_length(sample_area)
    print(result)