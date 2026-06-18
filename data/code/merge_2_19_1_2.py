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
    filtered.sort()
    return filtered, len(filtered)
def main():
    sample_data = [54321, 98760, -12345, 11111, 54321, 0, 98760]
    sorted_unique, count = optimize_sort_filter(sample_data)
    print(f"Processed {len(sorted_unique)} unique values.")
if __name__ == '__main__':
    main()