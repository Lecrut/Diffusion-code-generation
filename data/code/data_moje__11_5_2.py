def get_last_item(data_list):
    if not data_list:
        return None
    last_item = None
    for item in data_list:
        last_item = item
    return last_item

if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 60]
    result = get_last_item(sample_data)
    print(result)