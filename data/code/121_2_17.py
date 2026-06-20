def compare_lists_by_length(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    
    len1 = len(list1)
    len2 = len(list2)
    
    if len1 > len2:
        return list1
    elif len2 > len1:
        return list2
    else:
        return None

if __name__ == '__main__':
    l1 = [1, 2, 3]
    l2 = [4, 5]
    
    longer_list = compare_lists_by_length(l1, l2)
    
    if longer_list is not None:
        print(f"The longer list is: {longer_list}")
    else:
        print("Both lists are of the same length.")