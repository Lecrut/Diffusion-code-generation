def is_negative(number):
    return number < 0

if __name__ == '__main__':
    sample_values = [-10, -3, 0, 5, 20]
    results = {value: is_negative(value) for value in sample_values}
    print(results)