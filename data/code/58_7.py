def get_first_element(data):
    if not data:
        return None
    return data[0]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = ['a', 'b', 'c']
    empty_list = []
    single_item = [99]
    print(f"First element of {list1}: {get_first_element(list1)}")
    print(f"First element of {list2}: {get_first_element(list2)}")
    print(f"First element of {empty_list}: {get_first_element(empty_list)}")
    print(f"First element of {single_item}: {get_first_element(single_item)}")