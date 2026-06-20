def check_negative(numbers):
    return any(n < 0 for n in numbers)

if __name__ == '__main__':
    test_values = [1, -2, 3, 4, -5, 6]
    print(check_negative(test_values))