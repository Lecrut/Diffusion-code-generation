def find_last_element(data_list):
    if not data_list:
        return None
    return data_list[-1]

if __name__ == '__main__':
    DEFAULT_LIST = [10, 20, 30, 40, 50]
    last_element = find_last_element(DEFAULT_LIST)
    print(last_element)