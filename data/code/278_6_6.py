def format_and_print_numbers(numbers):
    for number in numbers:
        print(f"{number:.2f}")

if __name__ == '__main__':
    sample_values = [3.14159, 2.71828, 0.61803, 1.41421]
    format_and_print_numbers(sample_values)