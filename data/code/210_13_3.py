def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = [7, 3, 9, 1, 5]
    result = calculate_range(sample_numbers)
    print(result)