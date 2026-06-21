def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count if count > 0 else None

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(calculate_mean(sample_values))