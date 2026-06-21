MIDDLE_INDEX = lambda n: n // 2

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle_right = MIDDLE_INDEX(n)
    if n % 2 == 1:
        return sorted_numbers[middle_right]
    else:
        middle_left = middle_right - 1
        return (sorted_numbers[middle_left] + sorted_numbers[middle_right]) / 2

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    median_value = calculate_median(sample_values)
    print(median_value)