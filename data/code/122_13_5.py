def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 6.7]
    print(calculate_mean(sample_numbers))