import json
def simulate_source_1():
    return [
        {"id": 101, "name": "Apple", "category": "Fruit"},
        {"id": 102, "name": "Banana", "category": "Fruit"}
    ]
def simulate_source_2():
    return [
        {"id": 103, "name": "Orange", "category": "Citrus"},
        {"id": 104, "name": "Grapefruit", "category": "Citrus"},
        {"id": 105, "name": "Apple", "category": "Fruit"}                             
    ]
def simulate_source_3():
    return [
        {"id": 106, "name": "Mango", "category": "Tropical"},
        {"id": 107, "name": "Papaya", "category": "Tropical"}
    ]
def merge_and_deduplicate(data_sources):
    all_fruits = []
    for source in data_sources:
        if isinstance(source, str):
            try:
                parsed_data = json.loads(source)
            except json.JSONDecodeError:
                continue
        else:
            parsed_data = list(source)
        all_fruits.extend(parsed_data)
    seen_ids = {}
    unique_entries = []
    for entry in all_fruits:
        key = tuple(sorted(entry.items()))                                                                                                 
        if key not in seen_ids:
            seen_ids[key] = True
            unique_entries.append(entry)
    return unique_entries
def categorize_and_format(data):
    categorized_groups = []
    for entry in data:
        category_name = entry.get("category", "Unknown")
        if not any(group[0] == category_name for group in categorized_groups):
            new_group = [entry.copy()]
            categorized_groups.append((category_name, new_group))
    return [[group_name, items] for group_name, items in categorized_groups]
if __name__ == '__main__':
    sources_list = [simulate_source_1(), simulate_source_2(), simulate_source_3()]
    merged_data = merge_and_deduplicate(sources_list)
    final_output = categorize_and_format(merged_data)
    print(final_output)