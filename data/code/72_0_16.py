def compare_elements(list1, list2, index):
    try:
        element1 = list1[index]
    except IndexError:
        element1 = "Index out of bounds for list1"
    
    try:
        element2 = list2[index]
    except IndexError:
        element2 = "Index out of bounds for list2"
    
    return element1, element2

if __name__ == '__main__':
    LIST_A = [10, 20, 30, 40]
    LIST_B = [5, 15, 25, 35]
    INDEX_TO_CHECK = 2
    
    result = compare_elements(LIST_A, LIST_B, INDEX_TO_CHECK)
    
    print(f"List A: {LIST_A}")
    print(f"List B: {LIST_B}")
    print(f"Index: {INDEX_TO_CHECK}")
    print(f"Result: {result}")