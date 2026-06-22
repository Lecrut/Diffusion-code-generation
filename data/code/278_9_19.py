def format_complex_numbers(numbers):
    formatter = '{:.2f} + {:.2f}j'.format
    for number in numbers:
        print(formatter(number.real, number.imag))

if __name__ == '__main__':
    sample_numbers = [3+4j, 1-2j, 0+5j]
    format_complex_numbers(sample_numbers)