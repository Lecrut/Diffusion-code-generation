def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50.5]
    mean_value = calculate_mean(sample_values)
    print(mean_value)