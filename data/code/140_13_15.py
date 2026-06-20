def evaluate_condition(value, condition):
    conditions = {
        'greater than 10': lambda x: x > 10,
        'less than 0': lambda x: x < 0,
        'equal to active': lambda x: x == 'active'
    }
    return conditions.get(condition, lambda _: False)(value)

if __name__ == '__main__':
    test_values = [5, -3, 'active', 'inactive']
    for value in test_values:
        print(f"Value: {value}")
        print("Greater than 10:", evaluate_condition(value, 'greater than 10'))
        print("Less than 0:", evaluate_condition(value, 'less than 0'))
        print("Equal to active:", evaluate_condition(value, 'equal to active'))