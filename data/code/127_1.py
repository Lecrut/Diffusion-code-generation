def is_list_odd(data):
    for x in data:
        if x % 2 != 0:
            return True
    return False
if __name__ == '__main__':
    list1 = [2, 4, 6, 8]
    list2 = [1, 3, 5, 7]
    list3 = [2, 4, 6, 8, 9]
    list4 = []
    list5 = [10, 20, 30]
    print(f"list1: {is_list_odd(list1)}")
    print(f"list2: {is_list_odd(list2)}")
    print(f"list3: {is_list_odd(list3)}")
    print(f"list4: {is_list_odd(list4)}")
    print(f"list5: {is_list_odd(list5)}")