def get_median_element(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    if length % 2 == 1:
        return sorted_numbers[length // 2]
    else:
        mid1 = sorted_numbers[(length // 2) - 1]
        mid2 = sorted_numbers[length // 2]
        return (mid1 + mid2) / 2

if __name__ == '__main__':
    sample_data = [7, 1, 3, 9, 5, 2, 8, 4, 6]
    result = get_median_element(sample_data)
    print(result)