def analyze_conditions(conditions):
    if not conditions:
        return True
    and_results = []
    or_results = []
    for condition_key, condition_value in conditions.items():
        if condition_key == 'AND':
            and_results.append(condition_value)
        elif condition_key == 'OR':
            or_results.append(condition_value)
        else:
            and_results.append(condition_value)
            or_results.append(condition_value)
    final_and = all(and_results)
    final_or = any(or_results)
    if 'AND' in conditions and 'OR' in conditions:
        return final_and or final_or
    elif 'AND' in conditions:
        return final_and
    elif 'OR' in conditions:
        return final_or
    else:
        return True
if __name__ == '__main__':
    sample1 = {
        'A': True,
        'B': False,
        'AND': True,
        'OR': False
    }
    sample2 = {
        'P': True,
        'Q': False,
        'AND': True,
        'OR': True
    }
    sample3 = {
        'X': False,
        'Y': False,
        'AND': False,
        'OR': False
    }
    sample4 = {
        'C': True,
        'D': False,
        'AND': False,
        'OR': True
    }
    sample5 = {}
    print(f"Sample 1 Result: {analyze_conditions(sample1)}")
    print(f"Sample 2 Result: {analyze_conditions(sample2)}")
    print(f"Sample 3 Result: {analyze_conditions(sample3)}")
    print(f"Sample 4 Result: {analyze_conditions(sample4)}")
    print(f"Sample 5 Result: {analyze_conditions(sample5)}")