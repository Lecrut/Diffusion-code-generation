def is_positive(number):
    return number > 0

if __name__ == '__main__':
    sample_values = [0, -1, 5, -10, 23]
    results = {value: is_positive(value) for value in sample_values}
    print(results)