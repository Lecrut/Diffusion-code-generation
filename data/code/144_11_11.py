def implication_table(P, Q):
    return [[P, Q, not P or Q]]

if __name__ == '__main__':
    print(implication_table(True, True))
    print(implication_table(True, False))
    print(implication_table(False, True))
    print(implication_table(False, False))