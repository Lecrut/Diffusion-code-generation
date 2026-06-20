import math

def compare_measurements(a, b):
    difference = a - b
    if b == 0:
        ratio = float('inf') if a > 0 else (float('-inf') if a < 0 else 0)
    else:
        ratio = a / b
    is_greater = a > b
    return difference, ratio, is_greater

if __name__ == '__main__':
    a = 10.0
    b = 5.0
    diff, rat, greater = compare_measurements(a, b)
    print(diff)
    print(rat)
    print(greater)