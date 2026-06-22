def reverse_integer(n):
    negative = n < 0
    absolute_value = abs(n)
    reversed_string = str(absolute_value)[::-1]
    reversed_integer = int(reversed_string)
    if negative:
        reversed_integer = -reversed_integer
    return reversed_integer

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(120))
    print(reverse_integer(0))
    print(reverse_integer(-100))