def calculate_median(numbers):
    count = len(numbers)
    if count == 0:
        return None
    half = count // 2
    if count % 2 == 1:
        return numbers[half]
    left_val = numbers[half - 1]
    right_val = numbers[half]
    return (left_val + right_val) / 2.0

if __name__ == '__main__':
    values = [99, 12, 45, 7, 88, 34, 61]
    median_odd = calculate_median(values)
    print(median_odd)
    even_values = [100, 200, 300, 400]
    median_even = calculate_median(even_values)
    print(median_even)