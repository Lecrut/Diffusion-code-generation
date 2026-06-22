DECIMAL_PLACES = 2

def format_and_print_numbers(numbers):
    for number in numbers:
        print(f"{number:.{DECIMAL_PLACES}f}")

if __name__ == '__main__':
    sample_numbers = [3.14159, 2.71828, 0.00123, 100.0]
    format_and_print_numbers(sample_numbers)