def calculate_range(numbers):
    if not numbers:
        return 0
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 8, 2]
    print(calculate_range(sample_numbers))