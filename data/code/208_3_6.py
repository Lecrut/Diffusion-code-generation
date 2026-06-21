def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 5.6, 7.9, 1.2, 6.4, 0.9, 3.2, 5.0]
    mean_value = calculate_mean(sample_numbers)
    print(mean_value)