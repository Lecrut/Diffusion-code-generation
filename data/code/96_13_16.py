def evaluate_conditions(conditions):
    result = True
    for condition in conditions:
        if not condition[0]:
            result &= condition[1]
        else:
            result |= condition[1]
    return result

if __name__ == '__main__':
    sample_conditions = [
        (True, False),
        (False, True),
        (True, True)
    ]
    print(evaluate_conditions(sample_conditions))