def sum_digits(n):
    return eval('+'.join(str(abs(n))))

if __name__ == '__main__':
    print(sum_digits(123))
    print(sum_digits(456))
    print(sum_digits(-789))