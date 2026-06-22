def calculate_global_average(data_dict):
    total_sum = 0
    total_elements = 0
    for key, value_list in data_dict.items():
        total_sum += sum(value_list)
        total_elements += len(value_list)
    return total_sum / total_elements if total_elements > 0 else 0

if __name__ == '__main__':
    sample_data = {
        'group1': [1, 2, 3],
        'group2': [4, 5, 6],
        'group3': [7, 8, 9]
    }
    print(calculate_global_average(sample_data))