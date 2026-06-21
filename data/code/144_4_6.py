def implication_table():
    for A in [False, True]:
        for B in [False, True]:
            print(f"{A} -> {B}: {not A or B}")

if __name__ == '__main__':
    implication_table()