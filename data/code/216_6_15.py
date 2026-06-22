def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return float(numbers[n // 2])
    else:
        middle_left_value = numbers[n // 2 - 1]
        middle_right_value = numbers[n // 2]
        return (middle_left_value + middle_right_value) / 2.0

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.9, 5.1]
    print(calculate_median(sample_values))