def remove_duplicates(item_names):
    seen = set()
    unique_items = []
    for item in item_names:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    return unique_items

if __name__ == '__main__':
    sample_items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Apple"]
    print(remove_duplicates(sample_items))