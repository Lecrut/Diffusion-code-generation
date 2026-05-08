import random
def check_boolean_condition(value: bool, threshold: bool) -> bool:
    return value == threshold
def simulate_boolean_checks(input_a: bool, input_b: bool) -> tuple[bool, bool]:
    result_a = check_boolean_condition(input_a, True)
    result_b = check_boolean_condition(input_b, False)
    return result_a, result_b
if __name__ == '__main__':
    sample_a = True
    sample_b = False
    outcome_a, outcome_b = simulate_boolean_checks(sample_a, sample_b)
    comparison_result = outcome_a == outcome_b
    print(f"Input A: {sample_a}")
    print(f"Input B: {sample_b}")
    print(f"Outcome A (Check against True): {outcome_a}")
    print(f"Outcome B (Check against False): {outcome_b}")
    print(f"Are the outcomes equal? {comparison_result}")