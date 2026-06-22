def reverse_digits(n: int) -> int:
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

if __name__ == '__main__':
    print(reverse_digits(12345))
    print(reverse_digits(987654321))
    print(reverse_digits(1001))