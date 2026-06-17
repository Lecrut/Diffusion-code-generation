import json
def simulate_source_1():
    return [
        {"id": 1, "fruit": "apple", "category": "red"},
        {"id": 2, "fruit": "banana", "category": "yellow"}
    ]
def simulate_source_2():
    return [
        {"id": 3, "fruit": "orange", "category": "citrus"},
        {"id": 1, "fruit": "apple", "category": "red"}
    ]
def merge_and_deduplicate(data_sources):
    all_data = []
    for source in data_sources:
        all_data.extend(source)
    unique_ids = set()
    deduplicated_list = []
    seen_fruits = set()
    for item in all_data:
        if id(item) not in unique_ids and item["fruit"] not in seen_fruits:
            unique_ids.add(item["id"])
            seen_fruits.add(item["fruit"])
            deduplicated_list.append(item)
    return deduplicated_list
def group_by_category(data):
    groups = {}
    for item in data:
        cat = item["category"]
        if cat not in groups:
            groups[cat] = []
        groups[cat].append([item])                                         
    return [groups[k] for k in sorted(groups.keys())]
if __name__ == '__main__':
    sources = [simulate_source_1(), simulate_source_2()]
    merged_data = merge_and_deduplicate(sources)
    final_output = group_by_category(merged_data)
    print(final_output)