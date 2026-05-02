def get_last_item(data):
    if not data:
        return None
    return data[-1]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b', 'c']
    list3 = []
    list4 = [42]
    list5 = []
    print(get_last_item(list1))
    print(get_last_item(list2))
    print(get_last_item(list3))
    print(get_last_item(list4))
    print(get_last_item(list5))