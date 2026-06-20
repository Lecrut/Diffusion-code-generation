def evaluate_condition(value, condition):
    conditions = {
        'greater than 10': lambda x: x > 10,
        'less than 0': lambda x: x < 0,
        'equal to active': lambda x: x == 'active'
    }
    return conditions.get(condition, lambda _: False)(value)

if __name__ == '__main__':
    test_values = [5, -3, 'active', 'inactive']
    test_conditions = ['greater than 10', 'less than 0', 'equal to active', 'equal to inactive']
    
    results = {f'{value} {condition}': evaluate_condition(value, condition) for value in test_values for condition in test_conditions}
    print(results)