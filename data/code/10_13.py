def get_head(data_list):
    if data_list:
        return data_list[0]
    return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    print(get_head(sample_list))
    empty_list = []
    print(get_head(empty_list))