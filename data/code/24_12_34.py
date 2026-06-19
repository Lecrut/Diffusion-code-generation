def check_negativity(number):
    return number < 0

if __name__ == '__main__':
    sample_values = [10, -5, 0, -3.5, 2.7]
    results = {value: check_negativity(value) for value in sample_values}
    print(results)