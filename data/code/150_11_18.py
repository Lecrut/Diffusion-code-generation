def filter_out_value(lst, value):
    return [item for item in lst if item != value]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 30, 60, 70, 80, 90, 30]
    value_to_filter = 30
    filtered_result = filter_out_value(sample_list, value_to_filter)
    print(filtered_result)