import sys
def optimize_sort_filter(data: list[int]) -> tuple[list[int], int]:
    if not data:
        return [], 0
    seen = set()
    filtered = []
    for item in data:
        if item not in seen:
            seen.add(item)
            filtered.append(item)
    try:
        result = sorted(filtered)
    except TypeError:
        raise ValueError("Input must contain only integers")
    return result, len(result)
if __name__ == '__main__':
    sample_data = [3, 1, 4, 5, 9, 2, 6] + [-10, -5, 0, 7] * 1000
    sorted_unique, count = optimize_sort_filter(sample_data)
    print(f"Sorted unique elements: {sorted_unique}")
    print(f"Count of unique elements: {count}")