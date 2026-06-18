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
        result = sorted(filtered, reverse=True)
    except TypeError as e:
        raise ValueError("Input must contain only integers") from e
    return result, len(result)
def main():
    sample_data = [3, 1, 4, 5, 9, 2, 6] * (sys.getrecursionlimit() // 2 + 1000)
    sorted_unique, count = optimize_sort_filter(sample_data[:int(1e7)])
    print(f"Processed {len(sorted_unique)} unique integers.")
    print(f"Total elements processed: {count}")
if __name__ == '__main__':
    main()