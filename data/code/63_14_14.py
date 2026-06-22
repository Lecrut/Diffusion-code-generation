def reverse_integer_digits(n):
    if n < 0:
        return -int('-'.join(str(-n))[::-1])
    return int(str(n)[::-1])

if __name__ == '__main__':
    print(reverse_integer_digits(123))
    print(reverse_integer_digits(-456))
    print(reverse_integer_digits(1200))
    print(reverse_integer_digits(0))