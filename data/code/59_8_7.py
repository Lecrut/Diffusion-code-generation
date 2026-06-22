def sum_of_digits(n):
    return sum(eval(c) for c in str(abs(n)))

if __name__ == '__main__':
    print(sum_of_digits(12345))
    print(sum_of_digits(-987))
    print(sum_of_digits(0))