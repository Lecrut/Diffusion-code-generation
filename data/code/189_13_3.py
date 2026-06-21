def filter_out_value(target_list, value_to_exclude):
    filtered_list = [element for element in target_list if element != value_to_exclude]
    return filtered_list

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50, 60]
    value_to_eliminate = 30
    updated_list = filter_out_value(sample_values, value_to_eliminate)
    print(f"Original List: {sample_values}")
    print(f"Value to Exclude: {value_to_eliminate}")
    print(f"Updated List: {updated_list}")