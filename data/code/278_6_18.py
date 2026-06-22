def format_and_print_numbers(numbers):
    for number in numbers:
        print(f"{number:.2f}")

if __name__ == '__main__':
    sample_floats = [3.14159, 2.71828, 0.00123, 42.0]
    format_and_print_numbers(sample_floats)