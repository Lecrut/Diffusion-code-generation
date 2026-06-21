def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 6.7, 5.0, 9.2, 8.3, 7.4, 1.0, 2.5]
    mean_value = calculate_mean(sample_numbers)
    print(mean_value)