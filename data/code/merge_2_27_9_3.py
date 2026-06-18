import json
def simulate_source_1():
    return [
        {"id": 101, "name": "Apple", "category": "Fruit"},
        {"id": 102, "name": "Banana", "category": "Fruit"}
    ]
def simulate_source_2():
    return [
        {"id": 103, "name": "Orange", "category": "Citrus"},
        {"id": 104, "name": "Apple", "category": "Fruit"}
    ]
def merge_and_deduplicate(data_sources):
    all_fruits = []
    seen_ids = set()
    for source in data_sources:
        for item in source:
            if item["id"] not in seen_ids:
                seen_ids.add(item["id"])
                all_fruits.append(item)
    return all_fruits
def categorize_and_format(fruit_list):
    grouped = {}
    for fruit in fruit_list:
        cat = fruit.get("category", "Unknown")
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append([fruit["id"], fruit["name"]])
    return [grouped[key] for key in sorted(grouped.keys())]
if __name__ == '__main__':
    sources = [simulate_source_1(), simulate_source_2()]
    fruits = merge_and_deduplicate(sources)
    result = categorize_and_format(fruits)
    output_str = json.dumps(result, indent=4)