def is_odd(number):
    return number % 2 != 0

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results = {value: is_odd(value) for value in sample_values}
    print(results)