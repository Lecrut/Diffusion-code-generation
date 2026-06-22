def sum_digits(n):
    return sum(eval(c) for c in str(n) if c.isdigit())

if __name__ == '__main__':
    print(sum_digits(12345))
    print(sum_digits(987))
    print(sum_digits(0))