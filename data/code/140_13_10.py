def evaluate_condition(value, condition):
    conditions = {
        'greater than 10': lambda x: x > 10,
        'less than 0': lambda x: x < 0,
        'equal to active': lambda x: x == 'active'
    }
    if condition not in conditions:
        raise ValueError(f"Invalid condition: {condition}")
    return conditions[condition](value)

if __name__ == '__main__':
    print(evaluate_condition(5, 'greater than 10'))
    print(evaluate_condition(-3, 'less than 0'))
    print(evaluate_condition('active', 'equal to active'))