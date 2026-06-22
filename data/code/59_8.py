def sum_of_digits(n):
    return eval('+' + ''.join(str(abs(n))))

if __name__ == '__main__':
    print(sum_of_digits(123))
    print(sum_of_digits(4567))
    print(sum_of_digits(0))
    print(sum_of_digits(-987))