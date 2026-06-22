def is_odd(number):
    result = number & 1
    return result == 1

if __name__ == '__main__':
    test_values = [10, 23, 45, 68, 97, 100, 201]
    odd_check_results = {value: is_odd(value) for value in test_values}
    print(odd_check_results)