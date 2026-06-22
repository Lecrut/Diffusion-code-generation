def sum_of_digits(n):
    s = str(n)
    return eval('+'.join(s))

if __name__ == '__main__':
    print(sum_of_digits(123))
    print(sum_of_digits(4567))
    print(sum_of_digits(0))
    print(sum_of_digits(999))