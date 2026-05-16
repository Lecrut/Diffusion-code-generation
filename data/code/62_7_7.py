def find_second_element(data):
    if len(data) < 2:
        return None
    else:
        return data[1]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20]
    list3 = [5]
    list4 = []
    list5 = [99]
    print(f"Second element of {list1}: {find_second_element(list1)}")
    print(f"Second element of {list2}: {find_second_element(list2)}")
    print(f"Second element of {list3}: {find_second_element(list3)}")
    print(f"Second element of {list4}: {find_second_element(list4)}")
    print(f"Second element of {list5}: {find_second_element(list5)}")