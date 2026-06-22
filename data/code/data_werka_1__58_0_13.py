def retrieve_first_element(data_sequence):
    return data_sequence[0]

if __name__ == '__main__':
    SAMPLE_LIST = [5, 15, 25, 35]
    first_item = retrieve_first_element(SAMPLE_LIST)
    print(first_item)