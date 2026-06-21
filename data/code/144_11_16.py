def implication_table():
    return [(P, Q, not P or Q) for P in [True, False] for Q in [True, False]]

if __name__ == '__main__':
    print(implication_table())