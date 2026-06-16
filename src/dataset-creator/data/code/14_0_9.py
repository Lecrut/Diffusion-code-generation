def remove_duplicates_preserve_order(arr):
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_array = [5, 3, 1, 9, 2, 6, 8, 7, 4]
    unique_items = remove_duplicates_preserve_order(sample_array)
    print(unique_items)