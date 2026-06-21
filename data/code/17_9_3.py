def get_last_item(data_list):
    return data_list[-1]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_last_item(sample_data)
    print(result)