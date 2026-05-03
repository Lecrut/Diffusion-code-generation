import numpy as np
def is_greater(a, b):
    return a > b
if __name__ == '__main__':
    a_val = 10
    b_val = 5
    result1 = is_greater(a_val, b_val)
    print(f"is_greater({a_val}, {b_val}) is: {result1}")
    a_val = 3
    b_val = 7
    result2 = is_greater(a_val, b_val)
    print(f"is_greater({a_val}, {b_val}) is: {result2}")
    a_val = 10
    b_val = 10
    result3 = is_greater(a_val, b_val)
    print(f"is_greater({a_val}, {b_val}) is: {result3}")
    a_val = -2
    b_val = -5
    result4 = is_greater(a_val, b_val)
    print(f"is_greater({a_val}, {b_val}) is: {result4}")