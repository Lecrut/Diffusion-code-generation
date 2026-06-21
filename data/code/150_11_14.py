def remove_value(lst, value):
    return [item for item in lst if item != value]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 10]
    value_to_remove = 10
    filtered_list = remove_value(sample_list, value_to_remove)
    print(filtered_list)