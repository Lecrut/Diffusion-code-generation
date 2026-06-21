def find_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = data.copy()
    sorted_data.sort()
    mid_index = n // 2
    if n % 2 == 1:
        median = sorted_data[mid_index]
    else:
        median = (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2.0
    return median

if __name__ == '__main__':
    sample_list = [3.5, 1.2, 8.9, 4.1, 2.3]
    print(f"Sample List: {sample_list}")
    median = find_median(sample_list)
    print(f"Median: {median}")