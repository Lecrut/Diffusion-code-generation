import numpy as np
def calculate_difference_of_extremes(a: float, b: float) -> float:
    return np.abs(a - b)
if __name__ == '__main__':
    value1 = 25.5
    value2 = 15.0
    result1 = calculate_difference_of_extremes(value1, value2)
    print(f"Difference between {value1} and {value2}: {result1}")
    value3 = -10.2
    value4 = 4.8
    result2 = calculate_difference_of_extremes(value3, value4)
    print(f"Difference between {value3} and {value4}: {result2}")
    value5 = 0.0
    value6 = 100.0
    result3 = calculate_difference_of_extremes(value5, value6)
    print(f"Difference between {value5} and {value6}: {result3}")