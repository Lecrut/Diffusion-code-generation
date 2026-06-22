def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n == 0:
        return None
    elif n % 2 == 1:
        median_index = n // 2
        return sorted_numbers[median_index]
    else:
        mid1_index = (n - 1) // 2
        mid2_index = n // 2
        return (sorted_numbers[mid1_index] + sorted_numbers[mid2_index]) / 2

if __name__ == '__main__':
    sample_data1 = [1, 3, 5, 7, 9]
    sample_data2 = [1, 2, 3, 4, 5, 6]
    sample_data3 = [10, 20, 30]

    print(find_median(sample_data1))
    print(find_median(sample_data2))
    print(find_median(sample_data3))