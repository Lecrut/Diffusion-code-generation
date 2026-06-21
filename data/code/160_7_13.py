def remove_duplicates(item_names):
    seen = set()
    unique_items = []
    for name in item_names:
        if name not in seen:
            seen.add(name)
            unique_items.append(name)
    return unique_items

if __name__ == '__main__':
    sample_items = ["apple", "banana", "cherry", "date", "elderberry", "apple"]
    cleaned_list = remove_duplicates(sample_items)
    print(cleaned_list)