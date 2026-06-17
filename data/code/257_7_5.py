import numpy as np
def calculate_difference_of_extremes(a: float, b: float) -> float:
    return np.abs(a - b)
if __name__ == '__main__':
    a_val = 25.5
    b_val = 15.5
    result1 = calculate_difference_of_extremes(a_val, b_val)
    print(f"Difference between {a_val} and {b_val}: {result1}")
    a_val = -10.0
    b_val = 4.0
    result2 = calculate_difference_of_extremes(a_val, b_val)
    print(f"Difference between {a_val} and {b_val}: {result2}")
    a_val = 100.0
    b_val = 50.0
    result3 = calculate_difference_of_extremes(a_val, b_val)
    print(f"Difference between {a_val} and {b_val}: {result3}")