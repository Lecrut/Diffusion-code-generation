def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n == 0:
        return None
    elif n % 2 == 1:
        median_index = n // 2
        return sorted_numbers[median_index]
    else:
        mid1_index = n // 2 - 1
        mid2_index = n // 2
        median_value = (sorted_numbers[mid1_index] + sorted_numbers[mid2_index]) / 2.0
        return median_value
if __name__ == '__main__':
    sample_data1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_median(sample_data1))