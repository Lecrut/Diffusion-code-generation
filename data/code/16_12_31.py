def is_positive(number):
    if number <= 0:
        return False
    return True

if __name__ == '__main__':
    test_values = [-10, -1, 0, 0.5, 3, 100]
    results = {value: is_positive(value) for value in test_values}
    print(results)