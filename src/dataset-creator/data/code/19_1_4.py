import sys
def process_large_array(data: list[int]) -> tuple[list[int], int]:
    if not data:
        return [], 0
    filtered = [x for x in data if isinstance(x, (int, float)) and -1e9 < x <= 1e9]
    sorted_data = sorted(filtered)
    count = len(sorted_data)
    return sorted_data, count
if __name__ == '__main__':
    sample_values = [50, -3.7, 'text', None, 25, float('inf'), 100]
    result_list, total_count = process_large_array(sample_values)
    print(f"Processed {total_count} valid integers.")