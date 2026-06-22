def reverse_integer(n):
    negative = n < 0
    n = abs(n)
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    if negative:
        reversed_num = -reversed_num
    return reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(0))
    print(reverse_integer(1534236469))