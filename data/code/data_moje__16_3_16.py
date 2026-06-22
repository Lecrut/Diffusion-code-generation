def get_first_item(data_list):
    return data_list[0] if data_list else None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_first_item(sample_list)
    print(result)