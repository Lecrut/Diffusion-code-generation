import math
def calculate_length_ratio(length1: float, length2: float) -> float:
    if length2 == 0.0:
        return float('inf') if length1 != 0.0 else float('nan')
    return length1 / length2
if __name__ == '__main__':
    test_length1 = 10.0
    test_length2 = 3.0
    result = calculate_length_ratio(test_length1, test_length2)
    print(result)
    test_length1 = 0.0
    test_length2 = 5.0
    result = calculate_length_ratio(test_length1, test_length2)
    print(result)
    test_length1 = 0.0
    test_length2 = 0.0
    result = calculate_length_ratio(test_length1, test_length2)
    print(result)
    test_length1 = 1.0
    test_length2 = -2.0
    result = calculate_length_ratio(test_length1, test_length2)
    print(result)