def retrieve_first_item(list_data):
    return list_data[0] if list_data else None

if __name__ == '__main__':
    test_list = [99, 88, 77, 66]
    first_item = retrieve_first_item(test_list)
    print(first_item)