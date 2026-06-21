def calculate_mean(numbers):
    total = 0
    count = len(numbers)
    for number in numbers:
        total += number
    return total / count if count > 0 else float('nan')

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(calculate_mean(sample_data))