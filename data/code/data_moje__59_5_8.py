def digit_generator(number):
    for digit in str(abs(number)):
        yield int(digit)

def sum_digits(number):
    return sum(digit_generator(number))

if __name__ == '__main__':
    sample_number = 12345
    print(sum_digits(sample_number))