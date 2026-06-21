def check_contradictions(table1, table2):
    for row in range(len(table1)):
        if table1[row] != table2[row]:
            return False
    return True

if __name__ == '__main__':
    sample_table1 = [True, False, True, False]
    sample_table2 = [False, True, False, True]
    print(check_contradictions(sample_table1, sample_table2))