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
    sample_input = "hello world"
    sample_rule = "swap"
    try:
        input_string = sys.stdin.read().strip()
        if not input_string:
            input_string = sample_input
        manipulation_rule = sample_rule
        result = apply_case_manipulation(input_string, manipulation_rule)
        print(result)
    except Exception as e:
        pass