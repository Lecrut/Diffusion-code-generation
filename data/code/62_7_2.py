def find_second_element(data, index=0):
    if len(data) < 2:
        return None
    if index == 1:
        return data[1]
    return find_second_element(data, index + 1)
if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [5, 15]
    list3 = [7]
    list4 = [100]
    list5 = [99, 1]
    print(f"Second element of {list1}: {find_second_element(list1)}")
    print(f"Second element of {list2}: {find_second_element(list2)}")
    print(f"Second element of {list3}: {find_second_element(list3)}")
    print(f"Second element of {list4}: {find_second_element(list4)}")
    print(f"Second element of {list5}: {find_second_element(list5)}")