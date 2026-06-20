def is_negative(num):
    return num < 0

if __name__ == '__main__':
    test_values = [-5, 3, 0, -1.5]
    results = {value: is_negative(value) for value in test_values}
    print(results)