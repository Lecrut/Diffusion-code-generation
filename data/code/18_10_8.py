import numpy as np
def is_greater(a: float, b: float) -> bool:
    return a > b
if __name__ == '__main__':
    a_val = 10.5
    b_val = 5.0
    result1 = is_greater(a_val, b_val)
    print(f"is_greater({a_val}, {b_val}): {result1}")
    a_val = 3.14
    b_val = 3.14
    result2 = is_greater(a_val, b_val)
    print(f"is_greater({a_val}, {b_val}): {result2}")
    a_val = 20
    b_val = 25
    result3 = is_greater(a_val, b_val)
    print(f"is_greater({a_val}, {b_val}): {result3}")
    a_val = -1
    b_val = -5
    result4 = is_greater(a_val, b_val)
    print(f"is_greater({a_val}, {b_val}): {result4}")