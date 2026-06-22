def validate_input(data):
    for item in data:
        if not isinstance(item, complex):
            raise ValueError("All items must be complex numbers")

def print_complex_numbers(numbers):
    validate_input(numbers)
    for number in numbers:
        print(f"{number.real} + {number.imag}j")

if __name__ == '__main__':
    sample_numbers = [3+4j, 1-2j, 0+5j]
    print_complex_numbers(sample_numbers)