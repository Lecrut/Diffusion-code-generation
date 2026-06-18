import collections
def organize_data(data_list, group_by_key):
    grouped_data = collections.defaultdict(list)
    for item in data_list:
        if group_by_key in item:
            key = item[group_by_key]
            grouped_data[key].append(item)
        else:
            grouped_data[None].append(item)
    return dict(grouped_data)
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "category": "A", "value": 100},
        {"id": 2, "category": "B", "value": 250},
        {"id": 3, "category": "A", "value": 150},
        {"id": 4, "category": "C", "value": 300},
        {"id": 5, "category": "B", "value": 200},
        {"id": 6, "category": "A", "value": 120}
    ]
    grouping_criterion = "category"
    organized_result = organize_data(sample_data, grouping_criterion)
    print(organized_result)