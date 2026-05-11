from collections import defaultdict
def group_objects_by_attribute(data, key):
    grouped = defaultdict(list)
    for item in data:
        if hasattr(item, key):
            attribute_value = getattr(item, key)
            grouped[attribute_value].append(item)
        else:
            grouped["__missing__"].append(item)
    return dict(grouped)
if __name__ == '__main__':
    sample_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 30, "city": "New York"},
        {"name": "David", "city": "Chicago"},
        {"name": "Eve", "age": 25},
        {"name": "Frank", "city": "Los Angeles"}
    ]
    print("Grouping by 'age':")
    grouped_by_age = group_objects_by_attribute(sample_data, "age")
    for key, items in grouped_by_age.items():
        print(f"Age {key}: {items}")
    print("\nGrouping by 'city':")
    grouped_by_city = group_objects_by_attribute(sample_data, "city")
    for key, items in grouped_by_city.items():
        print(f"City {key}: {items}")
    print("\nGrouping by 'non_existent_key' (testing missing keys):")
    grouped_by_missing = group_objects_by_attribute(sample_data, "non_existent_key")
    for key, items in grouped_by_missing.items():
        print(f"Key {key}: {items}")