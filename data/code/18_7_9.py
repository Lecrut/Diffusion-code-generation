def get_middle_item(data_list):
    mid_index = len(data_list) // 2
    return data_list[mid_index]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60, 70]
    result = get_middle_item(sample_data)
    print(result)