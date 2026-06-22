def digit_generator(number):
    for digit in str(abs(number)):
        yield int(digit)

def sum_digits(number):
    return sum(digit_generator(number))

if __name__ == '__main__':
    sample_numbers = [123, 456, 789, 100, -42]
    for num in sample_numbers:
        digits = list(digit_generator(num))
        total = sum_digits(num)
        print(f"Number: {num}, Digits: {digits}, Sum: {total}")