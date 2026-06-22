def sum_of_digits(number: int) -> int:
    return sum([int(digit) for digit in str(number)])

if __name__ == '__main__':
    test_values = [123, 9999, 405]
    for value in test_values:
        result = sum_of_digits(value)
        print(result)