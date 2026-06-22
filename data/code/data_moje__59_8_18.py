def sum_digits(n):
    return eval('+'.join(str(abs(int(n)))))

if __name__ == '__main__':
    print(sum_digits(12345))