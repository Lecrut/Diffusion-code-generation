import math

def find_side_length(area):
    return math.sqrt(area)

if __name__ == '__main__':
    sample_area = 25
    side_length = find_side_length(sample_area)
    print(side_length)