def find_median_element(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    sorted_list = sorted(numbers)
    length = len(sorted_list)
    mid_index = length // 2
    if length % 2 == 1:
        return sorted_list[mid_index]
    return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    result = find_median_element(sample_data)
    print(result)