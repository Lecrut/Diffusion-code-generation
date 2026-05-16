def evaluate_boolean_expression(expression, values):
    tokens = expression.split(' & ')
    results = []
    for token in tokens:
        parts = token.split(' | ')
        sub_results = []
        for part in parts:
            sub_parts = part.split(' == ')
            if len(sub_parts) == 2:
                op = sub_parts[0].strip()
                val1_str = sub_parts[1].strip()
                if op == '==':
                    try:
                        val1 = values[int(val1_str)]
                        val2 = values[int(sub_parts[1].split('==')[1].strip())]
                        sub_results.append(val1 == val2)
                    except (ValueError, IndexError):
                        raise ValueError(f"Invalid index or comparison in: {part}")
                elif op == '!=':
                    try:
                        val1 = values[int(sub_parts[1].split('==')[1].strip())]
                        val2 = values[int(sub_parts[0].split('==')[1].strip())]
                        sub_results.append(val1 != val2)
                    except (ValueError, IndexError):
                        raise ValueError(f"Invalid index or comparison in: {part}")
                else:
                    raise ValueError(f"Unknown operator in: {part}")
            else:
                raise ValueError(f"Malformed expression segment: {part}")
        results.append(any(sub_results))
    return all(results)
def test_nested_boolean_logic(expression, values):
    try:
        result = evaluate_boolean_expression(expression, values)
        return result
    except ValueError as e:
        return f"Error: {e}"
if __name__ == '__main__':
    test_values = {
        1: True,
        2: False,
        3: True,
        4: False
    }
    test_cases = [
        ("1 == 3 & 2 == 4", test_values, True),
        ("1 == 2 | 3 == 4", test_values, False),
        ("1 == 3 & 1 != 3", test_values, False),
        ("1 == 1 | 2 == 2", test_values, True),
        ("1 == 3 & 3 == 3", test_values, True),
        ("1 == 2 | 3 == 1", test_values, False),
        ("1 == 3 & 2 == 3", test_values, False),
        ("1 == 1 | 2 == 1", test_values, True),
        ("1 == 4 & 2 == 4", test_values, False),
        ("1 == 1 | 2 == 2 | 3 == 3 | 4 == 4", test_values, True),
        ("1 == 3 & 2 == 2 | 4 == 4", test_values, True)
    ]
    for expression, values, expected in test_cases:
        actual = test_nested_boolean_logic(expression, values)
        status = "PASS" if actual == expected else "FAIL"
        print(f"Expression: '{expression}'")
        print(f"  Expected: {expected}, Actual: {actual} [{status}]\n")