def generate_implication_table():
    implication_table = {}
    for A in [False, True]:
        for B in [False, True]:
            result = "True" if not A or B else "False"
            implication_table[(A, B)] = result
    return implication_table

if __name__ == '__main__':
    table = generate_implication_table()
    print(table)