def validate_condition(value, condition):
    if not isinstance(condition, str) or condition not in ['greater than 10', 'less than 0', 'equal to active']:
        raise ValueError("Invalid condition provided")

def evaluate_condition(value, condition):
    conditions = {
        'greater than 10': lambda x: x > 10,
        'less than 0': lambda x: x < 0,
        'equal to active': lambda x: x == 'active'
    }
    return conditions.get(condition, lambda _: False)(value)

if __name__ == '__main__':
    try:
        print(evaluate_condition(5, 'greater than 10'))
        print(evaluate_condition(-3, 'less than 0'))
        print(evaluate_condition('active', 'equal to active'))
        print(evaluate_condition('inactive', 'equal to active'))
    except ValueError as e:
        print(e)