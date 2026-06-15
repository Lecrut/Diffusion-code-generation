import collections
def organize_data(data_list, criterion_key):
    grouped_data = collections.defaultdict(list)
    for item in data_list:
        if criterion_key in item:
            group_key = item[criterion_key]
            grouped_data[group_key].append(item)
        else:
            grouped_data["uncategorized"].append(item)
    return dict(grouped_data)
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "category": "A", "value": 100},
        {"id": 2, "category": "B", "value": 250},
        {"id": 3, "category": "A", "value": 150},
        {"id": 4, "category": "C", "value": 300},
        {"id": 5, "category": "B", "value": 200},
        {"id": 6, "category": "A", "value": 120},
        {"id": 7, "type": "D", "value": 400}
    ]
    grouping_criterion = "category"
    organized_result = organize_data(sample_data, grouping_criterion)
    print(organized_result)