def sum_digits(n):
    num = abs(n)
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

if __name__ == '__main__':
    print(sum_digits(12345))
    print(sum_digits(-9876))
    print(sum_digits(0))