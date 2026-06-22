def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.9, 5.1, 0.7, 6.3, 3.1, 2.2, 4.5]
    print(calculate_median(sample_values))