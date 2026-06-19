import math

def find_side_length(area):
    return math.sqrt(area)

if __name__ == '__main__':
    test_area = 49.0
    side_length = find_side_length(test_area)
    print(f'Side Length: {side_length}')