def sort_by_value_descending(data):
    return sorted(data, key=lambda x: x['value'], reverse=True)
if __name__ == '__main__':
    sample_list = [
        {'name': 'A', 'value': 30},
        {'name': 'B', 'value': 10},
        {'name': 'C', 'value': 20},
        {'name': 'D', 'value': 40}
    ]
    sorted_list = sort_by_value_descending(sample_list)
    print(sorted_list)