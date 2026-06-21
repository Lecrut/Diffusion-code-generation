def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 5.6, 7.9, 1.2, 6.3, 0.9, 2.5, 3.1]
    print(calculate_mean(sample_numbers))