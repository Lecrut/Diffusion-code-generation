def sum_digits(n):
    return sum(int(d) for d in str(abs(n)))

if __name__ == '__main__':
    print(sum_digits(1234))
    print(sum_digits(-567))
    print(sum_digits(0))
    print(sum_digits(10000000000000000000000000000))