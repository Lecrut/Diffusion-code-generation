def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 4, 2, 8, 6]
    result = calculate_range(sample_numbers)
    print(result)