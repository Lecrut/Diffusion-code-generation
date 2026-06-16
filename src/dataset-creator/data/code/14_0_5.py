def remove_duplicates_preserve_order(sequence):
    seen = set()
    result = []
    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [5, 3, 1, 4, 2, 5, 7, 8, 9, 6]
    unique_items = remove_duplicates_preserve_order(sample_data)
    print(unique_items)