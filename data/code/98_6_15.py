TARGET_STR = "SUCCESS"
MIN_VALUE = 5
MAX_VALUE = 15
DIFF_THRESHOLD = 10

def evaluate_scenario(reference_string, target_value, comparison_value):
    string_match = (reference_string == TARGET_STR)
    value_in_range = (MIN_VALUE <= target_value <= MAX_VALUE)
    numerical_inequality = (abs(target_value - comparison_value) > DIFF_THRESHOLD)
    
    if string_match and value_in_range and numerical_inequality:
        return "Conditions satisfied."
    return "Conditions not satisfied."

if __name__ == '__main__':
    result = evaluate_scenario("SUCCESS", 10, 25)
    print(result)