def evaluate_condition(condition_string):
    if not condition_string:
        return False
    parts = condition_string.lower().split()
    if len(parts) == 0:
        return False
    conditions = []
    for part in parts:
        if part == 'and':
            conditions.append('and')
        elif part == 'or':
            conditions.append('or')
        else:
            conditions.append(part)
    if not conditions:
        return False
    result = None
    current_state = None
    for i, part in enumerate(conditions):
        if part in ('and', 'or'):
            if i == 0:
                continue
            if len(conditions) <= i:
                raise ValueError("Syntax error: 'and' or 'or' found without a preceding condition.")
            operator = part
            operand = conditions[i-1]
            if current_state is None:
                raise ValueError(f"Syntax error: Operator '{operator}' found without a preceding condition.")
            if operator == 'and':
                if not evaluate_simple_condition(current_state):
                    result = False
                else:
                    result = True
                current_state = result
            elif operator == 'or':
                if not evaluate_simple_condition(current_state):
                    result = False
                else:
                    result = True
                current_state = result
            else:
                raise ValueError(f"Syntax error: Unknown operator '{operator}'.")
        else:
            try:
                value = evaluate_simple_condition(part)
                if current_state is None:
                    current_state = value
                else:
                    if part == 'and' or part == 'or':
                        raise ValueError(f"Syntax error: Unexpected token '{part}'.")
                    if part == 'and':
                        current_state = current_state and value
                    elif part == 'or':
                        current_state = current_state or value
                    else:
                        raise ValueError(f"Syntax error: Missing operator between conditions.")
            except ValueError:
                raise ValueError(f"Invalid condition format: {part}")
    if current_state is not None:
        return current_state
    return False
def evaluate_simple_condition(condition):
    if condition.startswith('a'):
        return True
    if condition.startswith('b'):
        return False
    return False
if __name__ == '__main__':
    test_cases = [
        ("A", True),
        ("B", False),
        ("A and B", True),
        ("B and A", True),
        ("A or B", True),
        ("B or A", True),
        ("A and B and A", True),
        ("A or B or A", True),
        ("A and not B", False),                                                                                      
        ("A and B and C", False),
        ("A and not A", False),
        ("A and B and not A", False),
        ("A and B and A or B", True),
        ("A and B and A or B and C", True)
    ]
    print("--- Testing Simple Conditions ---")
    for input_str, expected in test_cases:
        try:
            result = evaluate_condition(input_str)
            status = "PASS" if result == expected else f"FAIL (Expected: {expected}, Got: {result})"
            print(f"Input: '{input_str}' -> Result: {result} [{status}]")
        except ValueError as e:
            print(f"Input: '{input_str}' -> ERROR: {e}")
        except Exception as e:
            print(f"Input: '{input_str}' -> UNEXPECTED EXCEPTION: {e}")
    print("\n--- Testing Error Handling ---")
    error_cases = [
        "A and",
        "or B",
        "A and and B",
        "A or or B"
    ]
    for input_str in error_cases:
        try:
            evaluate_condition(input_str)
            print(f"Input: '{input_str}' -> FAIL (Did not raise error)")
        except ValueError as e:
            print(f"Input: '{input_str}' -> Caught expected error: {e}")
        except Exception as e:
            print(f"Input: '{input_str}' -> Caught unexpected error: {e}")