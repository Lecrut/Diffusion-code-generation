def is_positive(number):
    return number > 0

if __name__ == '__main__':
    sample_values = {
        'positive': 10,
        'negative': -5,
        'zero': 0,
        'another_positive': 3,
        'another_negative': -1
    }
    results = {key: is_positive(value) for key, value in sample_values.items()}
    print(results)