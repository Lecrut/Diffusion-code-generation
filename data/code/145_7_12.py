def compute_nested_if_else(conditions):
    result = True
    for condition in conditions:
        if condition == 'AND':
            result &= conditions.pop()
        elif condition == 'OR':
            result |= conditions.pop()
        else:
            result = condition
    return result

if __name__ == '__main__':
    sample_conditions = [
        True,
        False,
        'AND',
        'OR',
        False
    ]
    print(compute_nested_if_else(sample_conditions))