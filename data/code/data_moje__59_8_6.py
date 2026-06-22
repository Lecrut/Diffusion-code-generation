def sum_digits(n):
    return eval("+".join(str(n)))

if __name__ == '__main__':
    print(sum_digits(12345))
    print(sum_digits(-10))
    print(sum_digits(99))