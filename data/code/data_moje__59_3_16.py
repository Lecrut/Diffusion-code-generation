def sum_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

if __name__ == '__main__':
    print(sum_digits(12345))
    print(sum_digits(9876543210))
    print(sum_digits(-42))