import operator

if __name__ == '__main__':
    operators = {
        'greater_than': operator.gt,
        'less_than': operator.lt,
        'equal_to': operator.eq
    }
    
    values = [(10, 5), (3, 10), (10, 10)]
    
    for a, b in values:
        results = {key: func(a, b) for key, func in operators.items()}
        print(f"Is {a} greater than {b}? {results['greater_than']}")
        print(f"Is {a} less than {b}? {results['less_than']}")
        print(f"Is {a} equal to {b}? {results['equal_to']}")