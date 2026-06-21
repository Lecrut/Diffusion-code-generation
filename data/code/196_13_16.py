if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    
    def validate_lists(list1, list2):
        if not isinstance(list1, list) or not isinstance(list2, list):
            raise ValueError("Both inputs must be lists.")
    
    def append_lists_in_place(list1, list2):
        validate_lists(list1, list2)
        list1 += list2
    
    append_lists_in_place(list1, list2)
    print("Updated List 1:", list1)