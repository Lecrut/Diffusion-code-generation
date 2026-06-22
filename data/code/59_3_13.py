def sum_digits(n):
    n = abs(n)
    return sum([int(digit) for digit in str(n)])

if __name__ == '__main__':
    result = sum_digits(123456789)
    print(result)
    result = sum_digits(-98765)
    print(result)
    result = sum_digits(0)
    print(result)