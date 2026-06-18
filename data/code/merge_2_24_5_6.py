def sort_and_filter(items):
    if not items:
        return []
    filtered = [item for item in items if isinstance(item, (int, float)) and 0 < item <= 100]
    sorted_items = sorted(filtered)
    return sorted_items
if __name__ == '__main__':
    sample_data = [5.5, "apple", -3, 200, 7, None, 98.6, "banana", 42]
    result = sort_and_filter(sample_data)
    print(result)