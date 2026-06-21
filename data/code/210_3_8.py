def calculate_range(numbers):
    if not numbers:
        return None
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 5, 22, 8, 15]
    result = calculate_range(sample_numbers)
    print(result)