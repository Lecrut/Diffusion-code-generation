def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(calculate_median(sample_values))