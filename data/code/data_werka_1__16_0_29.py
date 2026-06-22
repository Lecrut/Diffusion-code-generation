def is_positive(number):
    return number > 0

if __name__ == '__main__':
    sample_values = [0, -1, 0.5, 100, -0.001]
    results = {value: is_positive(value) for value in sample_values}
    print(results)