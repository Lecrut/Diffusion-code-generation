def sum_digits(n):
    return eval('+'.join(str(n)))

if __name__ == '__main__':
    print(sum_digits(1234))
    print(sum_digits(9876))