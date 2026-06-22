def cycle_and_double(numbers):
    if not all(isinstance(num, int) and num >= 0 for num in numbers):
        raise ValueError("All elements must be non-negative integers")
    return [number * 2 for number in numbers]

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    doubled_values = cycle_and_double(sample_values)
    for value in doubled_values:
        print(value)