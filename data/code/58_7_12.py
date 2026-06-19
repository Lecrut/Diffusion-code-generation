def get_first_element(data):
    if not data:
        return None
    return data[0]

if __name__ == '__main__':
    list1 = [5, 6, 7, 8]
    list2 = ['x', 'y', 'z']
    empty_list = []
    single_item = [123]
    
    print(f"First element of {list1}: {get_first_element(list1)}")
    print(f"First element of {list2}: {get_first_element(list2)}")
    print(f"First element of {empty_list}: {get_first_element(empty_list)}")
    print(f"First element of {single_item}: {get_first_element(single_item)}")