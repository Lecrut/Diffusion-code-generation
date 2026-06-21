def range_of_numbers(numbers):
    if not numbers:
        return None
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 7.8, 0.9]
    print(range_of_numbers(sample_values))