def sum_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total

if __name__ == '__main__':
    result = sum_digits(12345)
    print(result)