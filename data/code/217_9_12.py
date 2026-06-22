import operator

COMPARATORS = {
    'greater_than': operator.gt,
    'less_than': operator.lt,
    'equal_to': operator.eq
}

if __name__ == '__main__':
    a = 10
    b = 5
    c = 3
    
    results = []
    for key, func in COMPARATORS.items():
        if key == 'greater_than':
            results.append(f"Is {a} strictly greater than {b}? {func(a, b)}")
        elif key == 'less_than':
            results.append(f"Is {c} strictly less than {b}? {func(c, b)}")
        elif key == 'equal_to':
            results.append(f"Is {a} equal to {c}? {func(a, c)}")
    
    for result in results:
        print(result)