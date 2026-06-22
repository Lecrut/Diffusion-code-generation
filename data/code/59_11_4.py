def digit_sum(n):
    if n < 0:
        n = -n
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    print(digit_sum(0))
    print(digit_sum(123))
    print(digit_sum(987654321098765432))
    print(digit_sum(-456))