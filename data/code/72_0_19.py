def compare_elements(list1, list2, index):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Inputs must be lists")
    if not isinstance(index, int):
        raise ValueError("Index must be an integer")
    
    try:
        val1 = list1[index]
    except IndexError:
        val1 = None
    
    try:
        val2 = list2[index]
    except IndexError:
        val2 = None
    
    return val1, val2

if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [40, 50, 60]
    idx = 1
    result = compare_elements(list_a, list_b, idx)
    print(result)
    
    list_c = [100]
    list_d = [200, 300]
    idx2 = 5
    result2 = compare_elements(list_c, list_d, idx2)
    print(result2)