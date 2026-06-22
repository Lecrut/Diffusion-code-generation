def print_floats(numbers):
    for number in numbers:
        print(f"{number:.2f}")

if __name__ == '__main__':
    sample_values = [3.14159, 2.71828, 0.001, 123.45678]
    print_floats(sample_values)