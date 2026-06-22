def digit_generator(n):
    for digit in str(abs(n)):
        yield int(digit)

def sum_digits(n):
    return sum(digit_generator(n))

if __name__ == '__main__':
    print(sum_digits(12345))
    print(sum_digits(9876))
    print(sum_digits(1001))