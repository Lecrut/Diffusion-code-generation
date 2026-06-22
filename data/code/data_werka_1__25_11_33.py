def is_zero(x):
    return x == 0

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2.5, None, '', [], {}]
    results = {value: is_zero(value) for value in sample_values}
    print(results)