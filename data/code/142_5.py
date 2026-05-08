import random
def check_boolean_condition(value: bool, threshold: bool) -> bool:
    return value == threshold
def simulate_boolean_checks():
    check1_input = random.choice([True, False])
    check2_input = random.choice([True, False])
    threshold1 = True
    threshold2 = False
    result1 = check_boolean_condition(check1_input, threshold1)
    result2 = check_boolean_condition(check2_input, threshold2)
    comparison_result = result1 == result2
    print(f"Check 1 Input: {check1_input}, Threshold: {threshold1}, Result: {result1}")
    print(f"Check 2 Input: {check2_input}, Threshold: {threshold2}, Result: {result2}")
    print(f"Comparison (Result1 == Result2): {comparison_result}")
if __name__ == '__main__':
    simulate_boolean_checks()