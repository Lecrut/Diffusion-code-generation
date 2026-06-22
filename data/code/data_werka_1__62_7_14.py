def find_second_element(data):
    if len(data) < 2:
        raise IndexError("List has fewer than two elements")
    return _find_second_helper(data, 1)

def _find_second_helper(data, index):
    if index == 0:
        return data[0]
    elif index == 1:
        return data[1]
    else:
        return _find_second_helper(data, index - 1)

if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [5, 15]
    list3 = [7]
    list4 = [99]
    
    try:
        print(f"Second element of {list1}: {find_second_element(list1)}")
    except IndexError as e:
        print(f"Error for {list1}: {e}")
    
    try:
        print(f"Second element of {list2}: {find_second_element(list2)}")
    except IndexError as e:
        print(f"Error for {list2}: {e}")
    
    try:
        print(f"Second element of {list3}: {find_second_element(list3)}")
    except IndexError as e:
        print(f"Error for {list3}: {e}")
    
    try:
        print(f"Second element of {list4}: {find_second_element(list4)}")
    except IndexError as e:
        print(f"Error for {list4}: {e}")