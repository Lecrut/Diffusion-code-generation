def sum_digits(n):
    n = abs(n)
    return sum([int(digit) for digit in str(n)])

if __name__ == '__main__':
    print(sum_digits(12345))
    print(sum_digits(99999999999999999999))