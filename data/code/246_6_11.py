import sys

def sum_constants(a, b):
    return a + b

if __name__ == '__main__':
    CONSTANT_X = 42
    CONSTANT_Y = 98
    total_sum = sum_constants(CONSTANT_X, CONSTANT_Y)
    sys.stdout.write(str(total_sum))