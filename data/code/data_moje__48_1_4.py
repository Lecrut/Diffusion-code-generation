def find_largest_integer(numbers):
    return max(numbers) if numbers else None

if __name__ == '__main__':
    sample_numbers = [15, 42, 8, 99, 3, 67, 24, 100, 5]
    result = find_largest_integer(sample_numbers)
    print(result)