def sort_by_priority(data):
    return sorted(data, key=lambda x: (x['priority'], x['name']))
if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'priority': 3},
        {'name': 'Bob', 'priority': 1},
        {'name': 'Charlie', 'priority': 3},
        {'name': 'David', 'priority': 2},
        {'name': 'Eve', 'priority': 1}
    ]
    sorted_data = sort_by_priority(sample_data)
    for item in sorted_data:
        print(item)