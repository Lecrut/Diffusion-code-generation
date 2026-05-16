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
        raise ValueError(f"Unknown manipulation rule: {rule}")
if __name__ == '__main__':
    input_string = "Hello World"
    manipulation_rule = "swap"
    try:
        result = apply_case_manipulation(input_string, manipulation_rule)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)