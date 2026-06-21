def check_logical_contradictions(table1, table2):
    for row1, row2 in zip(table1, table2):
        if all(row1[i] != row2[i] for i in range(len(row1))):
            return True
    return False

if __name__ == '__main__':
    sample_table1 = [[True, False], [False, True]]
    sample_table2 = [[False, True], [True, False]]
    print(check_logical_contradictions(sample_table1, sample_table2))