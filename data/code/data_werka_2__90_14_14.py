OR_THRESHOLD_ZERO = 0
DEFAULT_VALUE = 42

def apply_logical_or(primary_value, fallback_value):
    if primary_value > OR_THRESHOLD_ZERO:
        computed = primary_value
    else:
        computed = fallback_value
    return computed

if __name__ == '__main__':
    first_input = 0
    second_input = DEFAULT_VALUE
    outcome = apply_logical_or(first_input, second_input)
    print(outcome)
    outcome_two = apply_logical_or(10, second_input)
    print(outcome_two)
    outcome_three = apply_logical_or(-5, -1)
    print(outcome_three)