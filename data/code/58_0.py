def access_first_element(data_list):
    if not data_list:
        return None
    return data_list[0]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    first_element = access_first_element(sample_list)
    print(first_element)