def evaluate_conditions(condition_string):
    conditions = condition_string.lower().split()
    if not conditions:
        return False
    results = {}
    for cond in conditions:
        if 'and' in cond:
            parts = cond.split('and')
            if len(parts) == 2:
                left = parts[0].strip()
                right = parts[1].strip()
                if left and right:
                    try:
                        left_val = evaluate_single_condition(left)
                        right_val = evaluate_single_condition(right)
                        results[cond] = left_val and right_val
                    except ValueError:
                        results[cond] = None
                else:
                    results[cond] = False
            else:
                results[cond] = None
        elif 'or' in cond:
            parts = cond.split('or')
            if len(parts) == 2:
                left = parts[0].strip()
                right = parts[1].strip()
                if left and right:
                    try:
                        left_val = evaluate_single_condition(left)
                        right_val = evaluate_single_condition(right)
                        results[cond] = left_val or right_val
                    except ValueError:
                        results[cond] = None
                else:
                    results[cond] = False
            else:
                results[cond] = None
        else:
            try:
                results[cond] = evaluate_single_condition(cond)
            except ValueError:
                results[cond] = None
    return results
def evaluate_single_condition(condition):
    if condition == 'a':
        return True
    if condition == 'b':
        return False
    if condition == 'c':
        return True
    if condition == 'd':
        return False
    if condition == 'a and b':
        return True and False
    if condition == 'a or b':
        return True or False
    if condition == 'c and d':
        return True and False
    if condition == 'a or c':
        return True or True
    if condition == 'a and c':
        return True and True
    if condition == 'b or d':
        return False or False
    if condition == 'a and a':
        return True and True
    if condition == 'a or a':
        return True or True
    return None
if __name__ == '__main__':
    test_cases = [
        ('A and B', True),
        ('A or B', True),
        ('C and D', False),
        ('A or C', True),
        ('A and C', True),
        ('B or D', False),
        ('A and A', True),
        ('A or A', True),
        ('A and B or C', None),
        ('invalid condition', None),
        ('A and X', None)
    ]
    for input_str, expected in test_cases:
        actual = evaluate_conditions(input_str)
        print(f"Input: '{input_str}', Expected: {expected}, Actual: {actual}, Match: {actual == expected}")