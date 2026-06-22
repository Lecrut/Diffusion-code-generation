def is_even(number):
    return number & 1 == 0

if __name__ == '__main__':
    test_cases = {
        'positive_even': 4,
        'positive_odd': 3,
        'zero': 0,
        'negative_even': -6,
        'negative_odd': -7
    }
    
    for description, value in test_cases.items():
        result = is_even(value)
        print(f"{description} ({value}) is even: {result}")