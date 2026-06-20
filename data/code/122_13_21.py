def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [2.3, 4.5, 6.7, 8.9]
    mean_value = calculate_mean(sample_numbers)
    print(mean_value)