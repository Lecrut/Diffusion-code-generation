def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    results = [is_even(val) for val in sample_values]
    for val, res in zip(sample_values, results):
        print(res)