def logic_sequence():
    bool_list1 = [True, False]
    bool_list2 = [False, True]
    for b1, b2 in zip(bool_list1, bool_list2):
        yield b1 and b2

if __name__ == '__main__':
    results = list(logic_sequence())
    print(results[0])