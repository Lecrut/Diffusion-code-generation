def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [5, 10, 15, 20]
    print(calculate_mean(sample_values))