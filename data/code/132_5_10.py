def logic_sequence():
    bool_list1 = [True, False]
    bool_list2 = [False, True]
    
    if not (isinstance(bool_list1, list) and isinstance(bool_list2, list)):
        raise ValueError("Inputs must be lists.")
    
    for b1, b2 in zip(bool_list1, bool_list2):
        yield b1 and b2

if __name__ == '__main__':
    print(list(logic_sequence()))