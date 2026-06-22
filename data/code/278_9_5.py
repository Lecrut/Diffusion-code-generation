def print_complex_numbers(numbers):
    for number in numbers:
        real_part = number.real
        imag_part = number.imag
        formatted_number = f"{real_part} + {imag_part}j"
        print(formatted_number)

if __name__ == '__main__':
    sample_numbers = [2+3j, 4-5j, -1+0j]
    print_complex_numbers(sample_numbers)