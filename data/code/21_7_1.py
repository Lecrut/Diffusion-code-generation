def sort_by_custom_rule(data_list, key_index):
    return sorted(data_list, key=lambda item: item[key_index], reverse=True)
if __name__ == '__main__':
    sample_data = [
        (10, 1),
        (5, 2),
        (20, 3),
        (15, 4)
    ]
    key = 0
    sorted_data = sort_by_custom_rule(sample_data, key)
    print(sorted_data)