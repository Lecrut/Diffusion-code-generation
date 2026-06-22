def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2.0
    else:
        return numbers[mid]

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 6.7, 5.9, 1.2, 7.3, 8.4, 9.0, 0.5]
    median = calculate_median(sample_values)
    print(median)