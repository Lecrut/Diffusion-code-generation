def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    print(digit_sum(12345))
    print(digit_sum(0))
    print(digit_sum(999))