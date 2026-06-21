def find_common_elements(list1, list2):
    if not all(isinstance(i, (list, tuple)) for i in [list1, list2]):
        raise ValueError("Both inputs must be lists or tuples")
    
    set1 = set(list1)
    set2 = set(list2)
    
    return sorted(set1.intersection(set2))

if __name__ == '__main__':
    list_a = ["apple", "banana", "cherry", "date"]
    list_b = ["banana", "date", "fig", "grape"]
    print(find_common_elements(list_a, list_b))