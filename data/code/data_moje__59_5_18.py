def digit_generator(number):
    for digit in str(abs(number)):
        yield int(digit)

def sum_digits(number):
    return sum(digit_generator(number))

if __name__ == '__main__':
    test_numbers = [123, -456, 0, 7890]
    for num in test_numbers:
        digits = list(digit_generator(num))
        total = sum_digits(num)
        print(f"Number: {num}, Digits: {digits}, Sum: {total}")