import math
NEGATIVE_AREA_THRESHOLD = 0

def find_side_length(area):
    if area < NEGATIVE_AREA_THRESHOLD:
        raise ValueError('Area cannot be negative')
    return math.sqrt(area)
if __name__ == '__main__':
    sample_area = 64.0
    side_length = find_side_length(sample_area)
    print(side_length)