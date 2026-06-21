def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(calculate_mean(sample_numbers))