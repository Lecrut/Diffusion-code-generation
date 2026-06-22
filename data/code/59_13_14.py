def sum_of_digits(number: int) -> int:
    return sum([int(digit) for digit in str(number)])

if __name__ == '__main__':
    print(sum_of_digits(123))
    print(sum_of_digits(456))
    print(sum_of_digits(987654321))