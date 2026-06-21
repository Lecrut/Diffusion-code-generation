def filter_out_string(data, target):
    filtered_data = [item for item in data if item != target]
    return filtered_data

if __name__ == '__main__':
    initial_list = ["apple", "banana", "cherry", "banana"]
    target_string = "banana"
    result_list = filter_out_string(initial_list, target_string)
    print(result_list)