def logic_sequence():
    bools1 = [True, False, True]
    bools2 = [False, True, False]
    for b1, b2 in zip(bools1, bools2):
        yield b1 and b2

if __name__ == '__main__':
    print(list(logic_sequence()))