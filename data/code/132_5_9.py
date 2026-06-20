def logic_sequence():
    BOOL_LIST1 = [True, False, True]
    BOOL_LIST2 = [False, True, False]
    for b1, b2 in zip(BOOL_LIST1, BOOL_LIST2):
        yield b1 and b2

if __name__ == '__main__':
    for result in logic_sequence():
        print(result)