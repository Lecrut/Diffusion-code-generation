def sum_digits(n):
    n = abs(n)
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

if __name__ == '__main__':
    print(sum_digits(12345))
    print(sum_digits(-98765))
    print(sum_digits(0))
    print(sum_digits(10000000000000000000000))