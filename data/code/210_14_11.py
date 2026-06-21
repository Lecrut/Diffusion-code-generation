def calculate_range(numbers):
    if not numbers:
        return 0
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = [5, 3, 9, 1, 7]
    print(calculate_range(sample_numbers))