def retrieve_second_entry(data_list):
    SECOND_INDEX = 1
    return data_list[SECOND_INDEX]

if __name__ == '__main__':
    demonstration_data = [10, 20, 30, 40, 50]
    second_entry = retrieve_second_entry(demonstration_data)
    print(second_entry)