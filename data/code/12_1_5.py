def get_median(lst):
    if not lst:
        raise ValueError("List cannot be empty")
    sorted_list = sorted(lst)
    n = len(sorted_list)
    mid_index = n // 2
    if n % 2 == 0:
        return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2
    return sorted_list[mid_index]

if __name__ == '__main__':
    data = [7, 1, 5, 9, 3, 8, 2]
    result = get_median(data)
    print(result)