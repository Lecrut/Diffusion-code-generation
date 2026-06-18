import json
def simulate_source_1():
    return [
        {"id": 101, "name": "Apple", "category": "Fruit"},
        {"id": 102, "name": "Banana", "category": "Fruit"}
    ]
def simulate_source_2():
    return [
        {"id": 103, "name": "Orange", "category": "Citrus"},
        {"id": 104, "name": "Grape", "category": "Berry"},
        {"id": 105, "name": "Apple", "category": "Fruit"}                 
    ]
def simulate_source_3():
    return [
        {"id": 106, "name": "Mango", "category": "Tropical"},
        {"id": 107, "name": "Banana", "category": "Fruit"}                              
    ]
def merge_and_deduplicate(sources):
    all_fruits = []
    for source in sources:
        all_fruits.extend(source)
    seen_ids = set()
    unique_entries = []
    for entry in all_fruits:
        if entry["id"] not in seen_ids:
            seen_ids.add(entry["id"])
            unique_entries.append(entry)
    return unique_entries
def categorize_and_format(data):
    grouped_data = {}
    for item in data:
        cat = item.get("category", "Unknown")
        if cat not in grouped_data:
            grouped_data[cat] = []
        grouped_data[cat].append(item)
    return [grouped_data.values()]
if __name__ == '__main__':
    sources_list = [simulate_source_1(), simulate_source_2(), simulate_source_3()]
    merged_fruits = merge_and_deduplicate(sources_list)
    final_output = categorize_and_format(merged_fruits)