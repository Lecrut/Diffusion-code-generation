def digit_generator(n):
    if n < 0:
        n = -n
    if n == 0:
        yield 0
        return
    while n > 0:
        yield n % 10
        n //= 10

def sum_digits(n):
    return sum(digit_generator(n))

if __name__ == '__main__':
    number = 12345
    digits = list(digit_generator(number))
    total = sum_digits(number)
    print(f"digits: {digits}")
    print(f"sum: {total}")