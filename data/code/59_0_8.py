def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    print(sum_of_digits(12345))
    print(sum_of_digits(999))
    print(sum_of_digits(100000))
    print(sum_of_digits(7))