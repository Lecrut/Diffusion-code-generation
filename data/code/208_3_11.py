def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 5.6, 7.2, 9.0, 1.3, 6.5, 8.4, 2.9]
    print(calculate_mean(sample_numbers))