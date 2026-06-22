def sum_digits(n):
    s = str(abs(n))
    return eval("+".join(s))

if __name__ == '__main__':
    print(sum_digits(12345))
    print(sum_digits(-678))
    print(sum_digits(0))