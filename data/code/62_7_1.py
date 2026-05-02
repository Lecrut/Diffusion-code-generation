def find_second_element(data, index=0):
    if len(data) < 2:
        raise IndexError("List has fewer than two elements")
    if index == 1:
        return data[1]
    return find_second_element(data, index + 1)
if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [5, 15]
    list3 = [7]
    list4 = [99]
    list5 = [1]
    print(f"Second element of {list1}: {find_second_element(list1)}")
    print(f"Second element of {list2}: {find_second_element(list2)}")
    try:
        print(f"Second element of {list3}: {find_second_element(list3)}")
    except IndexError as e:
        print(f"Error for {list3}: {e}")
    try:
        print(f"Second element of {list4}: {find_second_element(list4)}")
    except IndexError as e:
        print(f"Error for {list4}: {e}")
    try:
        print(f"Second element of {list5}: {find_second_element(list5)}")
    except IndexError as e:
        print(f"Error for {list5}: {e}")