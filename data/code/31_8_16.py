import math

def calculate_square_area(side_length):
    return float(math.pow(side_length, 2))

if __name__ == '__main__':
    print(calculate_square_area(5.5))
    print(calculate_square_area(3.0))
    print(calculate_square_area(1.234))