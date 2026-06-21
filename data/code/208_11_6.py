def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [10, 20.5, 30, 40.75]
    print(calculate_mean(sample_values))