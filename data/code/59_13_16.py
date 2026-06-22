def sum_of_digits(n):
    return sum([int(d) for d in str(n)])

if __name__ == '__main__':
    print(sum_of_digits(12345))
    print(sum_of_digits(98765))