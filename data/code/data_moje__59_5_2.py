def digit_generator(number):
    for digit in str(abs(number)):
        yield int(digit)

def sum_digits(number):
    return sum(digit_generator(number))

if __name__ == '__main__':
    sample_numbers = [123, 4567, -987, 10001]
    for num in sample_numbers:
        print(sum_digits(num))