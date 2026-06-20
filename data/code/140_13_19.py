def evaluate_condition(value, condition):
    conditions = {'greater_than_10': lambda v: v > 10, 'less_than_0': lambda v: v < 0, 'equal_to_active': lambda v: v == 'active'}
    return conditions.get(condition, lambda _: False)(value)
if __name__ == '__main__':
    print(evaluate_condition(5, 'greater_than_10'))
    print(evaluate_condition(-3, 'less_than_0'))
    print(evaluate_condition('active', 'equal_to_active'))
    print(evaluate_condition('inactive', 'equal_to_active'))