def is_odd(n):
    return n % 2 != 0

if __name__ == '__main__':
    sample_values = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'negative_one': -1,
        'negative_two': -2,
        'negative_three': -3
    }
    results = {key: is_odd(value) for key, value in sample_values.items()}
    print(results)