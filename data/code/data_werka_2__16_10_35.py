def is_positive(x):
    return x > 0

if __name__ == '__main__':
    test_values = {'positive': 5, 'negative': -3, 'zero': 0}
    for description, value in test_values.items():
        print(f"{description}: {is_positive(value)}")