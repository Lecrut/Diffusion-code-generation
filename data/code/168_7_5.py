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
        {"name": "Eve", "age": 25}
    ]
    key_to_group = "age"
    grouped_by_age = group_objects_by_attribute(sample_data, key_to_group)
    print(f"Grouped by {key_to_group}:")
    for group, items in grouped_by_age.items():
        print(f"  {key_to_group}={group}: {items}")
    key_to_group_missing = "occupation"
    grouped_by_occupation = group_objects_by_attribute(sample_data, key_to_group_missing)
    print(f"\nGrouped by {key_to_group_missing}:")
    for group, items in grouped_by_occupation.items():
        print(f"  {key_to_group_missing}={group}: {items}")