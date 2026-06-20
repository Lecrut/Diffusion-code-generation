def contains_negative(values):
    return any(value < 0 for value in values)

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3],
        [-1, 2, 3],
        [1, -2, 3],
        [1, 2, -3]
    ]
    
    results = [contains_negative(case) for case in test_cases]
    print(results)