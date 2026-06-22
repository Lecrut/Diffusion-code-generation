def reverse_integer(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

if __name__ == '__main__':
    print(reverse_integer(12345))
    print(reverse_integer(987654321))
    print(reverse_integer(100))