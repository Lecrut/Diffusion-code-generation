def remove_duplicates_preserve_order(values):
    seen = set()
    result = []
    for item in values:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [5, 3, 1, 9, 2, 6, 8, 4, 7] * 2 + [0, -1]
    unique_items = remove_duplicates_preserve_order(sample_data)
    print(unique_items)