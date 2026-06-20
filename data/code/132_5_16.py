def logic_sequence():
    bool_list1 = [True, False]
    bool_list2 = [False, True]
    
    def validate_lists(list1, list2):
        if not all(isinstance(x, bool) for x in list1):
            raise ValueError("First list must contain only boolean values")
        if not all(isinstance(x, bool) for x in list2):
            raise ValueError("Second list must contain only boolean values")
        if len(list1) != len(list2):
            raise ValueError("Both lists must have the same length")
    
    validate_lists(bool_list1, bool_list2)
    
    for b1, b2 in zip(bool_list1, bool_list2):
        yield b1 and b2

if __name__ == '__main__':
    results = list(logic_sequence())
    print(results)