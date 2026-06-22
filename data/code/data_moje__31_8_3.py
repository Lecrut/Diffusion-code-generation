import math

def calculate_square_area(side_length):
    return float(math.pow(side_length, 2))

if __name__ == '__main__':
    sample_side = 5.5
    result = calculate_square_area(sample_side)
    print(result)