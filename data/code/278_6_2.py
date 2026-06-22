def print_floats(numbers):
    for number in numbers:
        print(f"{number:.2f}")

if __name__ == '__main__':
    sample_numbers = [3.14159, 2.71828, 0.00123, 100.0]
    print_floats(sample_numbers)