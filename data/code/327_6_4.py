import math
def floor_ceiling_remainder(a, b):
    floor_a = math.floor(a)
    ceil_a = math.ceil(a)
    rem_a = a - floor_a
    floor_b = math.floor(b)
    ceil_b = math.ceil(b)
    rem_b = b - floor_b
    return (floor_a, ceil_a, rem_a, floor_b, ceil_b, rem_b)
if __name__ == '__main__':
    num1 = 5.7
    num2 = 3.2
    result = floor_ceiling_remainder(num1, num2)
    print(result)