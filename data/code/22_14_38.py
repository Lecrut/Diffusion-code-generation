ODD_THRESHOLD = 1

def is_odd(number):
    return number % 2 != ODD_THRESHOLD

if __name__ == '__main__':
    sample_values = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results = {value: is_odd(value) for value in sample_values}
    print(results)