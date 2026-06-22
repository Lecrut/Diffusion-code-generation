def reverse_integer(n: int) -> int:
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(456))
    print(reverse_integer(789))
    print(reverse_integer(1000))
    print(reverse_integer(1001))