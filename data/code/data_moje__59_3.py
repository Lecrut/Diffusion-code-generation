def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

if __name__ == '__main__':
    test_values = [12345, -9876543210, 0, 1000000000000000000]
    for value in test_values:
        result = sum_of_digits(value)
        print(result)