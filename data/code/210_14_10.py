def calculate_range(numbers):
    if not numbers:
        return 0
    return max(numbers) - min(numbers)
if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(calculate_range(sample_numbers))
    empty_input = []
    print(calculate_range(empty_input))