import sys
def optimize_sort_filter(data: list[int]) -> tuple[list[int], int]:
    if not data:
        return [], 0
    filtered = [x for x in data if isinstance(x, (int, float)) and -1e9 < x <= 1e9]
    sorted_data = sorted(filtered)
    count = len(sorted_data)
    return sorted_data, count
if __name__ == '__main__':
    sample_array = [3, 245, 876.0, -100, 'a', None, 99, float('inf'), 2]
    result_list, item_count = optimize_sort_filter(sample_array)
    print(f"Filtered and sorted array: {result_list}")
    print(f"Total valid items count: {item_count}")
    if sys.getsizeof(result_list) > 10 * (sys.maxsize // 2):
        result_str = ", ".join(map(str, result_list))
    else:
        result_str = " ".join(map(str, result_list))
    print(f"Memory efficient output string: {result_str}")