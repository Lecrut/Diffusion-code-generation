def check_negativity(number):
    return number < 0

if __name__ == '__main__':
    sample_values = [10, -5, 0.5, -3.2, 0]
    results = [check_negativity(value) for value in sample_values]
    print(results)