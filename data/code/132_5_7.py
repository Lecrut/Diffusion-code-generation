def logic_sequence():
    bool_list1 = [True, False, True]
    bool_list2 = [False, True, False]
    if len(bool_list1) != len(bool_list2):
        raise ValueError("Both lists must have the same length")
    for b1, b2 in zip(bool_list1, bool_list2):
        yield b1 and b2

if __name__ == '__main__':
    results = list(logic_sequence())
    print(results)