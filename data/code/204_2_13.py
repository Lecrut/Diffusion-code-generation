def find_median(values):
    sorted_values = sorted(values)
    length = len(sorted_values)
    mid = length // 2
    if length % 2 == 1:
        return sorted_values[mid]
    else:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2.0

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    median_result = find_median(sample_list)
    print(f"Median of {sample_list}: {median_result}")