def sum_of_digits(n):
    return sum([int(digit) for digit in str(n)])

if __name__ == '__main__':
    result = sum_of_digits(12345)
    print(result)
    result = sum_of_digits(98765)
    print(result)