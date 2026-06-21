def remove_duplicates(item_names):
    seen = set()
    result = []
    for item in item_names:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Apple"]
    cleaned_items = remove_duplicates(sample_items)
    print(cleaned_items)