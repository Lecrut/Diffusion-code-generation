def sum_of_digits(n):
    return eval('+'.join(c for c in str(abs(n)) if c.isdigit()))

if __name__ == '__main__':
    print(sum_of_digits(12345))
    print(sum_of_digits(-987))
    print(sum_of_digits(0))