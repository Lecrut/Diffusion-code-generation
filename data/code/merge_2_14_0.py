def remove_duplicates_preserve_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [5, 3, 1, 2, 4, 6, 7, 8, 9, 0]
    print(remove_duplicates_preserve_order(sample_data))