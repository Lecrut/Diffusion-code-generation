def sum_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return sum_digits(n // 10) + n % 10

if __name__ == '__main__':
    print(sum_digits(12345))
    print(sum_digits(987654321))
    print(sum_digits(0))
    print(sum_digits(-42))