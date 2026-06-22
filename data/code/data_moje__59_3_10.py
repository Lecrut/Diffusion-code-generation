def sum_digits(n):
    n = abs(n)
    return sum(int(d) for d in str(n))

if __name__ == '__main__':
    print(sum_digits(12345))
    print(sum_digits(9876543210))
    print(sum_digits(0))
    print(sum_digits(-42))