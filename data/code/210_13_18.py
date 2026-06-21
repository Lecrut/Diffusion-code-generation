def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 4, 3, 7, 5]
    print(calculate_range(sample_numbers))