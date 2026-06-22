def sum_digits(n):
    s = str(abs(n))
    return eval('+'.join(s))

if __name__ == '__main__':
    print(sum_digits(123))
    print(sum_digits(9876543210))
    print(sum_digits(0))
    print(sum_digits(-456))