def calculate_average(dict_of_lists):
    total_sum = 0
    total_elements = 0
    for key, value_list in dict_of_lists.items():
        total_sum += sum(value_list)
        total_elements += len(value_list)
    if total_elements == 0:
        return 0
    return total_sum / total_elements

if __name__ == '__main__':
    sample_dict = {
        'list1': [1, 2, 3],
        'list2': [4, 5, 6],
        'list3': [7, 8, 9]
    }
    print(calculate_average(sample_dict))