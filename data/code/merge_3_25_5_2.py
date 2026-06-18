import math

def is_zero(x):
    return abs(float(x)) < 1e-9 if x != float('inf') and x != -float('inf') else False

if __name__ == '__main__':
    print(is_zero(0.0))     # True
    print(is_zero(0))       # True
    print(is_zero(1e-15))   # True
    print(is_zero(1e-9))    # False