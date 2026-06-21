def check_contradictions(table1, table2):
    for row in zip(table1, table2):
        if all(row) or all(not x for x in row):
            return False
    return True

if __name__ == '__main__':
    table1 = [True, False, True, False]
    table2 = [False, True, False, True]
    print(check_contradictions(table1, table2))