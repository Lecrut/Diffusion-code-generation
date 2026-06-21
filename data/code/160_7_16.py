def remove_duplicates(items):
    seen = set()
    unique_items = []
    for item in items:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    return unique_items

if __name__ == '__main__':
    sample_names = ["Apple", "Banana", "Cherry", "Apple", "Banana"]
    cleaned_names = remove_duplicates(sample_names)
    print(cleaned_names)