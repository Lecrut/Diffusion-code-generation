def reverse_integer(n):
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10
    return reversed_n

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(456))
    print(reverse_integer(789))