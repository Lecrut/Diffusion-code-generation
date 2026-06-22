def print_complex_numbers(numbers):
    number_format = "{:.2f} + {:.2f}j"
    for number in numbers:
        formatted_number = number_format.format(number.real, number.imag)
        print(formatted_number)

if __name__ == '__main__':
    sample_numbers = [3+4j, 1-2j, 0+5j]
    print_complex_numbers(sample_numbers)