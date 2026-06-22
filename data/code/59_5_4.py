def digit_generator(number):
    if number < 0:
        number = -number
    if number == 0:
        yield 0
        return
    while number > 0:
        yield number % 10
        number //= 10

def sum_digits(number):
    return sum(digit_generator(number))

if __name__ == '__main__':
    sample_values = [12345, -9876, 0, 1001]
    for value in sample_values:
        digits = list(digit_generator(value))
        total = sum_digits(value)
        print(f"Number: {value}, Digits: {digits}, Sum: {total}")