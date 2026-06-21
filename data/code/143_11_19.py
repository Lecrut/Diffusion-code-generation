def check_contradiction(table1, table2):
    for row in range(len(table1)):
        if table1[row] != table2[row]:
            return True
    return False

if __name__ == '__main__':
    sample_table1 = [True, False, True]
    sample_table2 = [False, False, True]
    print(check_contradiction(sample_table1, sample_table2))