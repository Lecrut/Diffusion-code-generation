def get_first_item_safely(data_list):
    if not data_list:
        raise IndexError("List is empty")
    return data_list[0]

if __name__ == '__main__':
    SAMPLE_LIST = [1, 2, 3]
    EMPTY_LIST = []
    
    try:
        first_item = get_first_item_safely(SAMPLE_LIST)
        print(f"First item from sample list: {first_item}")
    except IndexError as e:
        print(f"Error retrieving from sample list: {e}")
    
    try:
        first_item_empty = get_first_item_safely(EMPTY_LIST)
        print(f"First item from empty list: {first_item_empty}")
    except IndexError as e:
        print(f"Error retrieving from empty list: {e}")