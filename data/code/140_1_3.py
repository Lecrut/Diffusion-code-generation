def analyze_conditions(conditions):
    if not conditions:
        return False
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
        return all(conditions.values())
if __name__ == '__main__':
    sample_conditions_1 = {
        'A': True,
        'B': False,
        'AND': True,
        'OR': False
    }
    sample_conditions_2 = {
        'X': True,
        'Y': True,
        'Z': False,
        'AND': True
    }
    sample_conditions_3 = {
        'P': False,
        'Q': True,
        'OR': True
    }
    sample_conditions_4 = {
        'A': True,
        'B': True,
        'AND': False,
        'OR': False
    }
    print(f"Result 1: {analyze_conditions(sample_conditions_1)}")
    print(f"Result 2: {analyze_conditions(sample_conditions_2)}")
    print(f"Result 3: {analyze_conditions(sample_conditions_3)}")
    print(f"Result 4: {analyze_conditions(sample_conditions_4)}")