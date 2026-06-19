def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    sample_values = [4, 7, 10, 13, 22]
    results = {value: is_even(value) for value in sample_values}
    print(results)