def exclude_value(input_list, value_to_exclude):
    return [element for element in input_list if element != value_to_exclude]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60]
    target_value = 30
    modified_data = exclude_value(sample_data, target_value)
    print(f"Original Data: {sample_data}")
    print(f"Target Value to Exclude: {target_value}")
    print(f"Modified Data: {modified_data}")