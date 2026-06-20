def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [2.5, 3.6, 4.1, 5.7]
    mean_value = calculate_mean(sample_numbers)
    print(mean_value)