def flatten_boolean_logic(a, b, c):
    return (a or b) and not (not a and not b) and c

if __name__ == '__main__':
    print(flatten_boolean_logic(True, False, True))