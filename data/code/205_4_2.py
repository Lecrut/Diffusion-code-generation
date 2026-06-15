def sort_by_value_descending(data):
    return sorted(data, key=lambda x: x['value'], reverse=True)
if __name__ == '__main__':
    sample_list = [
        {'value': 30},
        {'value': 10},
        {'value': 50},
        {'value': 20}
    ]
    sorted_list = sort_by_value_descending(sample_list)
    print(sorted_list)