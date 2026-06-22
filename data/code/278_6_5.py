def print_numbers(numbers):
    for number in numbers:
        print(f"{number:.2f}")

if __name__ == '__main__':
    sample_values = [3.14159, 2.71828, 1.61803]
    print_numbers(sample_values)