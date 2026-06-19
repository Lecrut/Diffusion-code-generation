def retrieve_first_item(data_list):
    if not data_list:
        raise IndexError("The list is empty, cannot retrieve the first item.")
    return data_list[0]

if __name__ == '__main__':
    sample_list_1 = [5, 15, 25]
    sample_list_2 = []

    try:
        first_item = retrieve_first_item(sample_list_1)
        print(f"First item from sample_list_1: {first_item}")
    except IndexError as e:
        print(e)

    try:
        first_item_empty = retrieve_first_item(sample_list_2)
        print(f"First item from sample_list_2: {first_item_empty}")
    except IndexError as e:
        print(e)