def calculate_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0.0

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = calculate_mean(sample_data)
    print(result)