def combine_booleans(a, b, c):
    return a and b or not c
if __name__ == '__main__':
    print(combine_booleans(True, False, True))
    print(combine_booleans(False, True, False))