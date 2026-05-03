def find_last_element(data_list):
    if not data_list:
        return None
    return data_list[-1]
if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    last_element = find_last_element(my_list)
    print(last_element)