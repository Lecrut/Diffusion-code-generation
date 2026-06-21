def flatten_logic(a, b, c):
    return (not a) or (b and not c)

if __name__ == '__main__':
    print(flatten_logic(True, False, True))
    print(flatten_logic(False, True, False))
    print(flatten_logic(True, True, True))
    print(flatten_logic(False, False, False))