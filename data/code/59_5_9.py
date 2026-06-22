def digits_generator(n):
    n = abs(int(n))
    if n == 0:
        yield 0
        return
    while n > 0:
        yield n % 10
        n //= 10

def sum_digits(n):
    return sum(digits_generator(n))

if __name__ == '__main__':
    sample_number = 12345
    result = sum_digits(sample_number)
    print(result)