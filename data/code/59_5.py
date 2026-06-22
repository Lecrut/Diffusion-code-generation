def digit_generator(n):
    n = abs(n)
    if n == 0:
        yield 0
        return
    while n > 0:
        yield n % 10
        n //= 10

def sum_digits(n):
    return sum(digit_generator(n))

if __name__ == '__main__':
    sample_numbers = [123, 4567, 987654321, 0, -42]
    for num in sample_numbers:
        digits = list(digit_generator(num))
        total = sum_digits(num)
        print(digits)
        print(total)