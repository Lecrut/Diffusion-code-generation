def calculate_nested_average(data_dict):
    total_sum = 0
    total_count = 0
    for key, values in data_dict.items():
        if isinstance(values, list) and values:
            total_sum += sum(values)
            total_count += len(values)
    return total_sum / total_count if total_count > 0 else 0
if __name__ == '__main__':
    sample_data = {'group1': [1, 2, 3], 'group2': [4, 5, 6, 7], 'group3': []}
    average = calculate_nested_average(sample_data)
    print(average)