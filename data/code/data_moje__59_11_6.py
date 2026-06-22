def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    print(digit_sum(123456789012345678))
    print(digit_sum(999999999999999999))
    print(digit_sum(1))
    print(digit_sum(1000000000000000000))