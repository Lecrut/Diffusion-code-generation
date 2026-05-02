def get_first_element(data_list):
    if not data_list:
        return None
    return data_list[0]
if __name__ == '__main__':
    list1 = [10, 20, 30]
    list2 = ['a', 'b', 'c']
    empty_list = []
    list3 = [42]
    print(f"First element of {list1}: {get_first_element(list1)}")
    print(f"First element of {list2}: {get_first_element(list2)}")
    print(f"First element of {empty_list}: {get_first_element(empty_list)}")
    print(f"First element of {list3}: {get_first_element(list3)}")