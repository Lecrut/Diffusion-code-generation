def get_last_item(data_list):
    if not data_list:
        return None
    return data_list[-1]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_last_item(sample_data)
    print(result)