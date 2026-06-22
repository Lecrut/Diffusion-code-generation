def sum_of_digits(n):
    return sum(int(c) for c in str(abs(n)))

if __name__ == '__main__':
    print(sum_of_digits(12345))
    print(sum_of_digits(-9876543210))