def is_odd(number):
    return number & 1 == 1

if __name__ == '__main__':
    sample_values = [0, 1, 2, 3, 4, 5, 10, 15, 16]
    results = {value: is_odd(value) for value in sample_values}
    print(results)