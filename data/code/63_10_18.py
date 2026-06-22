def reverse_integer(n):
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
    return reversed_n

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(4567))
    print(reverse_integer(1000))
    print(reverse_integer(987654321))