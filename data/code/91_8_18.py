def negate_value(flag):
    if not isinstance(flag, bool):
        raise ValueError("Input must be a boolean type")
    return not flag

def display_negation_results():
    test_flags = [True, False]
    for current_flag in test_flags:
        result = negate_value(current_flag)
        print(f"Original: {current_flag}, Negated: {result}")

if __name__ == '__main__':
    display_negation_results()