def is_odd(number):
    return number % 2 != 0

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2, -2, 3, -3]
    results = {value: is_odd(value) for value in sample_values}
    print(results)