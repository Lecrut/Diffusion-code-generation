def reverse_digits(n):
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n //= 10
    return result

if __name__ == '__main__':
    print(reverse_digits(12345))
    print(reverse_digits(9876543210))
    print(reverse_digits(1001))