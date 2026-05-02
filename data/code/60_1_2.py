def get_last_item(data):
    if not data:
        return None
    return data[-1]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b', 'c']
    empty_list = []
    single_item = [99]
    print(get_last_item(list1))
    print(get_last_item(list2))
    print(get_last_item(empty_list))
    print(get_last_item(single_item))