def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    mean_value = calculate_mean(sample_numbers)
    print(mean_value)