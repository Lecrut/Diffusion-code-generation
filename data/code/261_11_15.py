def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2.0
    else:
        return numbers[mid]

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.9, 5.6, 7.1, 0.9, 6.3, 2.1, 3.9]
    print(calculate_median(sample_values))