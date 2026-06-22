def evaluate_number_properties(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a numeric type")
    if value <= 0:
        return "Not positive"
    if value % 2 != 0:
        return "Odd"
    if value >= 100:
        return "Too large"
    return "Positive, even, and less than 100"

if __name__ == '__main__':
    test_cases = [42, -1, 99, 100, 200, 0.5]
    for case in test_cases:
        print(evaluate_number_properties(case))