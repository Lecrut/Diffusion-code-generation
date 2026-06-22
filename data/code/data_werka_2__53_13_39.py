import math

def calculate_side_length(area):
    if area < 0:
        raise ValueError('Area cannot be negative')
    return math.sqrt(area)
if __name__ == '__main__':
    sample_area1 = 16
    sample_area2 = 25
    sample_area3 = 81
    print(calculate_side_length(sample_area1))
    print(calculate_side_length(sample_area2))
    print(calculate_side_length(sample_area3))