import sys
def apply_case_manipulation(text, rule):
    if rule == 'swap':
        return text[::-1]
    elif rule == 'reverse':
        return text[::-1]
    elif rule == 'upper':
        return text.upper()
    elif rule == 'lower':
        return text.lower()
    else:
        raise ValueError(f"Unknown case manipulation rule: {rule}")
if __name__ == '__main__':
    sample_input = "Hello World"
    sample_rule = "swap"
    try:
        input_data = sys.stdin.read().strip()
        if not input_data:
            input_data = sample_input
        rule_to_apply = sample_rule
        result = apply_case_manipulation(input_data, rule_to_apply)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)