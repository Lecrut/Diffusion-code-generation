def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 6.7, 5.2, 9.0, 8.3, 7.6, 1.4, 2.9]
    print(calculate_mean(sample_values))