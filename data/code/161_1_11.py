def create_unique_item_list(item_objects):
    unique_names = set()
    for item in item_objects:
        unique_names.add(item.name)
    return list(unique_names)

if __name__ == '__main__':
    sample_items = [
        {"id": 1, "name": "banana"},
        {"id": 2, "name": "apple"},
        {"id": 3, "name": "cherry"},
        {"id": 4, "name": "date"},
        {"id": 5, "name": "elderberry"},
        {"id": 6, "name": "banana"}
    ]
    unique_items = create_unique_item_list(sample_items)
    print(unique_items)