def filter_duplicates(item_names):
    seen = set()
    cleaned_list = []
    for item in item_names:
        if item not in seen:
            seen.add(item)
            cleaned_list.append(item)
    return cleaned_list

if __name__ == '__main__':
    sample_items = ["apple", "banana", "apple", "orange", "banana", "grape"]
    print(filter_duplicates(sample_items))