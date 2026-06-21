def find_median(sorted_numbers):
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 1:
        return sorted_numbers[mid]
    else:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0

if __name__ == '__main__':
    sample_input = [10, 5, 20, 15, 30]
    number_list = sorted(sample_input)
    median_value = find_median(number_list)
    print(median_value)