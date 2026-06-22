def sum_digits(n):
    if n < 0:
        n = -n
    return sum(int(d) for d in str(n))

if __name__ == '__main__':
    print(sum_digits(12345))
    print(sum_digits(-6789))
    print(sum_digits(0))