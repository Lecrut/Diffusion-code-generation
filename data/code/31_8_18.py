import math

def square_area(side_length):
    return float(math.pow(side_length, 2))

if __name__ == '__main__':
    result = square_area(5.5)
    print(result)