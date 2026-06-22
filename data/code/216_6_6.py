def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    return (numbers[mid - 1] + numbers[mid]) / 2.0 if n % 2 == 0 else float(numbers[mid])

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.9, 5.1]
    print(calculate_median(sample_values))