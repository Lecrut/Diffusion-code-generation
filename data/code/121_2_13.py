MAX_LIST_SIZE = 100

def compare_lists(list1, list2):
    size1 = len(list1)
    size2 = len(list2)
    
    if size1 > MAX_LIST_SIZE or size2 > MAX_LIST_SIZE:
        raise ValueError("One of the lists exceeds the maximum allowed size.")
    
    if size1 == size2:
        return "Both lists have the same length."
    elif size1 > size2:
        return list1
    else:
        return list2

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [6, 7, 8, 9]
    
    longer_list = compare_lists(sample_list1, sample_list2)
    print(longer_list)