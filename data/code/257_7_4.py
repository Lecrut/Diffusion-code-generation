import numpy as np
def calculate_difference_of_extremes(a: float, b: float) -> float:
    return np.abs(a - b)
if __name__ == '__main__':
    a_val = 25.5
    b_val = 18.75
    result = calculate_difference_of_extremes(a_val, b_val)
    print(f"The difference between {a_val} and {b_val} is: {result}")
    a_val_neg = -100.0
    b_val_pos = 50.0
    result_neg = calculate_difference_of_extremes(a_val_neg, b_val_pos)
    print(f"The difference between {a_val_neg} and {b_val_pos} is: {result_neg}")
    a_val_equal = 42.0
    b_val_equal = 42.0
    result_equal = calculate_difference_of_extremes(a_val_equal, b_val_equal)
    print(f"The difference between {a_val_equal} and {b_val_equal} is: {result_equal}")