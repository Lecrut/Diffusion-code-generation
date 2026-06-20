def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count if count > 0 else 0

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(calculate_average(sample_numbers))