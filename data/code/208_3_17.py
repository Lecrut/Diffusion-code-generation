def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 6.7, 5.0, 9.2, 1.3, 8.4, 7.6, 2.9]
    mean_value = calculate_mean(sample_numbers)
    print(mean_value)