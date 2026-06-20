def find_longer_list(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    
    size1 = len(list1)
    size2 = len(list2)
    
    if size1 > size2:
        return list1
    elif size2 > size1:
        return list2
    else:
        return None

if __name__ == '__main__':
    l1 = [1, 2, 3]
    l2 = [4, 5, 6, 7]
    longer_list = find_longer_list(l1, l2)
    print(longer_list)