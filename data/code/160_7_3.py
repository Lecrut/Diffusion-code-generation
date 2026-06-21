def filter_duplicates(item_names):
    seen = set()
    result = []
    for item in item_names:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_items = ["apple", "banana", "apple", "orange", "banana", "grape"]
    print(filter_duplicates(sample_items))