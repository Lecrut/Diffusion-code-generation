def format_complex_numbers(numbers):
    for number in numbers:
        print(f"{number.real} + {number.imag}j")

if __name__ == '__main__':
    sample_numbers = [2+3j, -1+4j, 0-2j]
    format_complex_numbers(sample_numbers)