import math
def calculate_floor_ceiling_remainder(a, b):
    floor_a = math.floor(a)
    ceil_a = math.ceil(a)
    floor_b = math.floor(b)
    ceil_b = math.ceil(b)
    remainder = a - b * math.floor(a / b)
    return (floor_a, ceil_a, remainder)
if __name__ == '__main__':
    num1 = 10.7
    num2 = 3.4
    result = calculate_floor_ceiling_remainder(num1, num2)
    print(result)