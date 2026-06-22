def calculate_mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    result = calculate_mean(sample_numbers)
    print(result)