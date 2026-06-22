def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return sorted_numbers[n // 2]

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.9, 5.6, 0.7, 6.1, 3.2, 2.1, 4.5]
    print(calculate_median(sample_values))