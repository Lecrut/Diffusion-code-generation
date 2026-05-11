from collections import defaultdict
def group_objects_by_attribute(data, key_attribute):
    grouped_data = defaultdict(list)
    for item in data:
        if hasattr(item, key_attribute):
            key_value = getattr(item, key_attribute)
            grouped_data[key_value].append(item)
        else:
            grouped_data["__missing__"].append(item)
    return dict(grouped_data)
if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
        {'name': 'Charlie', 'age': 30, 'city': 'New York'},
        {'name': 'David', 'age': 35},
        {'name': 'Eve', 'city': 'Chicago'},
        {'name': 'Frank', 'age': 25, 'city': 'Los Angeles'},
    ]
    print("Grouping by 'city':")
    grouped_by_city = group_objects_by_attribute(sample_data, 'city')
    for city, items in grouped_by_city.items():
        print(f"City: {city}, Items: {items}")
    print("\nGrouping by 'age':")
    grouped_by_age = group_objects_by_attribute(sample_data, 'age')
    for age, items in grouped_by_age.items():
        print(f"Age: {age}, Items: {items}")
    print("\nGrouping by 'name' (demonstrating missing keys):")
    grouped_by_name = group_objects_by_attribute(sample_data, 'name')
    for name, items in grouped_by_name.items():
        print(f"Name: {name}, Items: {items}")