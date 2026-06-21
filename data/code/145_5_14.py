def flatten_logic(a, b, c):
    return (a or b) and c == ((not a) and (not b)) or c

if __name__ == '__main__':
    print(flatten_logic(True, False, True))
    print(flatten_logic(False, False, False))
    print(flatten_logic(True, True, False))