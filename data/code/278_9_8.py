COMPLEX_NUMBER_FORMAT = "{real} + {imag}j"

def print_complex_numbers(numbers):
    for number in numbers:
        print(COMPLEX_NUMBER_FORMAT.format(real=number.real, imag=number.imag))

if __name__ == '__main__':
    sample_numbers = [3+4j, 1-2j, 0+5j]
    print_complex_numbers(sample_numbers)