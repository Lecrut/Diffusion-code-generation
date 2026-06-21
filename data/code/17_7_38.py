def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    sample_values = [15, 22, -8, 1, 0, 99]
    results = {value: is_even(value) for value in sample_values}
    print(results)