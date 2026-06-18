import collections
def organize_data(data_list, key_field):
    grouped_data = collections.defaultdict(list)
    for item in data_list:
        if key_field in item:
            key = item[key_field]
            grouped_data[key].append(item)
        else:
            grouped_data["__uncategorized__"].append(item)
    return dict(grouped_data)
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "category": "A", "value": 100},
        {"id": 2, "category": "B", "value": 250},
        {"id": 3, "category": "A", "value": 150},
        {"id": 4, "category": "C", "value": 300},
        {"id": 5, "category": "B", "value": 200},
        {"id": 6, "category": "A", "value": 125},
    ]
    grouping_key = "category"
    organized_result = organize_data(sample_data, grouping_key)
    import json
    print(json.dumps(organized_result, indent=4))