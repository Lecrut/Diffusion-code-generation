def group_by_second_element(tuples_list):
    grouped_dict = {}
    for item in tuples_list:
        key, value = item
        if value not in grouped_dict:
            grouped_dict[value] = []
        grouped_dict[value].append(key)
    return grouped_dict

if __name__ == '__main__':
    sample_data = [('apple', 'fruit'), ('carrot', 'vegetable'), ('banana', 'fruit'), ('broccoli', 'vegetable'), ('orange', 'fruit')]
    grouped_result = group_by_second_element(sample_data)
    print(grouped_result)