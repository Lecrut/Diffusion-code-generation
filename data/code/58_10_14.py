FIRST_ITEM_INDEX = 0

def retrieve_first_item(lst):
    return lst[FIRST_ITEM_INDEX] if lst else None

if __name__ == '__main__':
    test_list = [9, 18, 27, 36, 45]
    print(retrieve_first_item(test_list))