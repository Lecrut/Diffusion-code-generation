def process_numbers(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return numbers[0], numbers[-1]

if __name__ == '__main__':
    sample_input = [10, 25, 30, 45, 50]
    first, last = process_numbers(sample_input)
    print(first, last)