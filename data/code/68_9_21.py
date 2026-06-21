def find_difference(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError('Both inputs must be numbers')
    return abs(num1 - num2)

if __name__ == '__main__':
    test_cases = {
        'case1': {'num1': 10, 'num2': 4},
        'case2': {'num1': -5, 'num2': 15},
        'case3': {'num1': 7.5, 'num2': 3.2},
        'case4': {'num1': 0, 'num2': 0},
    }
    
    for case_name, params in test_cases.items():
        try:
            result = find_difference(params['num1'], params['num2'])
            print(f"The absolute difference between {params['num1']} and {params['num2']} is: {result}")
        except ValueError as e:
            print(f"Error in {case_name}: {e}")