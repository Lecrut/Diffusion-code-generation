def digit_generator(number):
    number = abs(int(number))
    if number == 0:
        yield 0
        return
    while number > 0:
        yield number % 10
        number //= 10

def sum_digits(number):
    return sum(digit_generator(number))

if __name__ == '__main__':
    sample_numbers = [12345, 987654321, 0, -42]
    for n in sample_numbers:
        digits = list(digit_generator(n))
        total = sum_digits(n)
        print(f"Number: {n}, Digits: {digits}, Sum: {total}")