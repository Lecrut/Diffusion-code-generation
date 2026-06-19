def is_negative(number):
    return number < 0

if __name__ == '__main__':
    sample_values = [-1, 0, 1, -5.5, 3.2]
    results = [is_negative(value) for value in sample_values]
    print(results)