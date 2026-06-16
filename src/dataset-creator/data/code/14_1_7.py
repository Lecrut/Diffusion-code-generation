def filter_unique_elements(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [1, 2, 'apple', 3, 'banana', 4, 'apple', 5]
    unique_items = filter_unique_elements(sample_data)
    print(unique_items)