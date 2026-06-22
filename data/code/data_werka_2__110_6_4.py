def sort_unix_timestamps(timestamp_list):
    if not isinstance(timestamp_list, list):
        raise ValueError("Input must be a list")
    for item in timestamp_list:
        if not isinstance(item, int):
            raise ValueError("All elements must be integers")
    sorted_list = list(timestamp_list)
    n = len(sorted_list)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if sorted_list[j] < sorted_list[min_idx]:
                min_idx = j
        if min_idx != i:
            sorted_list[i], sorted_list[min_idx] = sorted_list[min_idx], sorted_list[i]
    return sorted_list

if __name__ == '__main__':
    raw_dates = [1700000000, 1600000000, 1800000000, 1500000000, 1650000000]
    ordered_dates = sort_unix_timestamps(raw_dates)
    print(ordered_dates)