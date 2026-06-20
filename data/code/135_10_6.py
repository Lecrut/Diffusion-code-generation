def are_equivalent(statement1, statement2):
    truth_table1 = {i: eval(statement1) for i in range(2)}
    truth_table2 = {i: eval(statement2) for i in range(2)}
    return truth_table1 == truth_table2

if __name__ == '__main__':
    sample_statement1 = 'x and y'
    sample_statement2 = 'y and x'
    print(are_equivalent(sample_statement1, sample_statement2))