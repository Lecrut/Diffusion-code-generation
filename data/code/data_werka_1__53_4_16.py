import math

def find_side_length(area):
    return math.sqrt(area)

if __name__ == '__main__':
    test_area = 36.0
    side_length_result = find_side_length(test_area)
    print(side_length_result)