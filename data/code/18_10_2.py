import numpy as np
def is_greater(a, b):
    return a > b
if __name__ == '__main__':
    print(f"is_greater(10, 5): {is_greater(10, 5)}")
    print(f"is_greater(5, 10): {is_greater(5, 10)}")
    print(f"is_greater(7.5, 7.5): {is_greater(7.5, 7.5)}")
    print(f"is_greater(-2, -5): {is_greater(-2, -5)}")
    print(f"is_greater(0, -1): {is_greater(0, -1)}")