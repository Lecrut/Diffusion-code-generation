def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n//2 - 1] + numbers[n//2]) / 2.0
    else:
        return numbers[n//2]

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 6.7, 5.9, 1.2, 7.3, 8.4, 0.9, 2.5]
    print(calculate_median(sample_values))