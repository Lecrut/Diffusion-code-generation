from collections import defaultdict
def group_objects_by_attribute(data, key):
    grouped = defaultdict(list)
    for obj in data:
        if hasattr(obj, key):
            attribute_value = getattr(obj, key)
            grouped[attribute_value].append(obj)
        else:
            grouped["__missing__"].append(obj)
    return dict(grouped)
if __name__ == '__main__':
    sample_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 30, "city": "New York"},
        {"name": "David", "city": "Chicago"},
        {"name": "Eve", "age": 28}
    ]
    key_to_group = "city"
    grouped_by_city = group_objects_by_attribute(sample_data, key_to_group)
    print(f"Grouped by '{key_to_group}':")
    for city, items in grouped_by_city.items():
        print(f"  {city}: {[item.get('name', 'Unknown') for item in items]}")
    key_to_group_missing = "occupation"
    grouped_by_occupation = group_objects_by_attribute(sample_data, key_to_group_missing)
    print(f"\nGrouped by '{key_to_group_missing}':")
    for occupation, items in grouped_by_occupation.items():
        print(f"  {occupation}: {[item.get('name', 'Unknown') for item in items]}")