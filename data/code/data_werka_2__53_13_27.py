import math

def calculate_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return math.sqrt(area)

if __name__ == '__main__':
    sample_area1 = 16
    sample_area2 = 25
    sample_area3 = 81

    side_length1 = calculate_side_length(sample_area1)
    side_length2 = calculate_side_length(sample_area2)
    side_length3 = calculate_side_length(sample_area3)

    print(side_length1)
    print(side_length2)
    print(side_length3)