def cycle_and_double(numbers):
    for number in numbers:
        if not isinstance(number, int) or number <= 0:
            raise ValueError("All elements must be positive integers")
        print(number * 2)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    cycle_and_double(sample_values)