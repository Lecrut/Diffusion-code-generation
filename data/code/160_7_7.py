def filter_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_items = ["apple", "banana", "apple", "orange", "banana", "grape"]
    cleaned_list = filter_duplicates(sample_items)
    print(cleaned_list)