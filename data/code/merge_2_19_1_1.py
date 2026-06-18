import sys
def optimize_sort_filter(data: list[int]) -> tuple[list[int], int]:
    if not data:
        return [], 0
    seen = set()
    filtered_unique = []
    for item in sorted(data):
        if item not in seen:
            seen.add(item)
            filtered_unique.append(item)
    return filtered_unique, len(seen)
if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    result_list, unique_count = optimize_sort_filter(sample_data)
    print(f"Unique sorted count: {unique_count}")
    print("Filtered list:", result_list)