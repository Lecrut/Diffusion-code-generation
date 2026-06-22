def print_complex_numbers(numbers):
    for number in numbers:
        print(f"{number.real} + {number.imag}j")

if __name__ == '__main__':
    sample_numbers = [3+4j, 1-2j, -1+0j]
    print_complex_numbers(sample_numbers)