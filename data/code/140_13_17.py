def evaluate_condition(value, condition):
    conditions = {'greater_than_10': lambda x: x > 10, 'less_than_0': lambda x: x < 0, 'equal_to_active': lambda x: x == 'active'}
    return conditions.get(condition, lambda _: False)(value)
if __name__ == '__main__':
    print(evaluate_condition(5, 'greater_than_10'))
    print(evaluate_condition(-3, 'less_than_0'))
    print(evaluate_condition('active', 'equal_to_active'))