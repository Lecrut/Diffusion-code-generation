def is_positive(number):
    return number > 0

if __name__ == '__main__':
    test_cases = {
        'zero': 0,
        'negative_one': -1,
        'positive_two_point_five': 2.5,
        'negative_three_six': -3.6,
        'hundred': 100
    }
    
    results = {name: is_positive(value) for name, value in test_cases.items()}
    print(results)