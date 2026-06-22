def count_digits(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count
if __name__ == '__main__':
    print(count_digits(12345))
    print(count_digits(-98765))
    print(count_digits(0))