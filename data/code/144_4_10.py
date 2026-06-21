def implication_table():
    for A in [False, True]:
        for B in [False, True]:
            print(f"{A} -> {B}: {'True' if not A or B else 'False'}")

if __name__ == '__main__':
    implication_table()