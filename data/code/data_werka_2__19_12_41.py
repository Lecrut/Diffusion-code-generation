def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_cases = {
        'zero': 0,
        'positive_even': 4,
        'positive_odd': 3,
        'negative_even': -6,
        'negative_odd': -5
    }
    
    results = {key: is_even(value) for key, value in test_cases.items()}
    print(results)