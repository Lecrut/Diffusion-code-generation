def evaluate_condition(value, condition):
    conditions = {
        'greater than 10': lambda x: x > 10,
        'less than 0': lambda x: x < 0,
        'equal to active': lambda x: x == 'active',
        'is even': lambda x: x % 2 == 0
    }
    return conditions.get(condition, lambda _: False)(value)

if __name__ == '__main__':
    test_values = [5, -3, 'active', 4]
    conditions = ['greater than 10', 'less than 0', 'equal to active', 'is even']
    
    results = {condition: evaluate_condition(value, condition) for value, condition in zip(test_values, conditions)}
    
    print(results)