def find_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    middle_index = n // 2
    if n % 2 == 1:
        return sorted_data[middle_index]
    else:
        lower_middle_index = middle_index - 1
        return (sorted_data[lower_middle_index] + sorted_data[middle_index]) / 2

if __name__ == '__main__':
    sample_list = [4, 7, 2, 5, 8]
    result = find_median(sample_list)
    print(result)