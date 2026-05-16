import numpy as np
def is_greater(a: float, b: float) -> bool:
    return a > b
if __name__ == '__main__':
    a1 = 10.5
    b1 = 5.0
    result1 = is_greater(a1, b1)
    print(f"Is {a1} > {b1}? {result1}")
    a2 = 3.14
    b2 = 3.14
    result2 = is_greater(a2, b2)
    print(f"Is {a2} > {b2}? {result2}")
    a3 = -5
    b3 = 0
    result3 = is_greater(a3, b3)
    print(f"Is {a3} > {b3}? {result3}")
    a4 = 100
    b4 = 99.99
    result4 = is_greater(a4, b4)
    print(f"Is {a4} > {b4}? {result4}")