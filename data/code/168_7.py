from collections import defaultdict
def group_objects_by_attribute(data_list, attribute):
    grouped_data = defaultdict(list)
    for item in data_list:
        key = item.get(attribute)
        if key is not None:
            grouped_data[key].append(item)
        else:
            grouped_data["__missing__"].append(item)
    return dict(grouped_data)
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "category": "A", "value": 100},
        {"id": 2, "category": "B", "value": 200},
        {"id": 3, "category": "A", "value": 150},
        {"id": 4, "value": 300},
        {"id": 5, "category": "C", "value": 50},
        {"id": 6, "category": "B", "value": 250},
        {"id": 7, "category": None, "value": 400},
    ]
    attribute_to_group = "category"
    grouped_result = group_objects_by_attribute(sample_data, attribute_to_group)
    print(grouped_result)