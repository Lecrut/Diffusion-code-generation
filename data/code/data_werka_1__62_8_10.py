def retrieve_second_entry(data_list):
    INDEX_SECOND = 1
    return data_list[INDEX_SECOND]

if __name__ == '__main__':
    demonstration_list = [3, 6, 9, 12, 15]
    second_value = retrieve_second_entry(demonstration_list)
    print(second_value)