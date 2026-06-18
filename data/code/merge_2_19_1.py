import sys
def process_large_array(data: list[int]) -> tuple[list[int], int]:
    if not data:
        return [], 0
    sorted_data = sorted(data)
    filtered_count = sum(1 for x in sorted_data if x > 0)
    return [x for x in sorted_data if x > 0], filtered_count
if __name__ == '__main__':
    sample_values = [-5, -2, 3, 8, 0, 7, -1, 4]
    result_list, count = process_large_array(sample_values)
    print(f"Filtered and sorted list: {result_list}")
    print(f"Count of positive integers: {count}")