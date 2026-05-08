def calculate_mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    mean_value = calculate_mean(sample_numbers)
    print(mean_value)