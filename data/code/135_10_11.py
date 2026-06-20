def are_equivalent(statement1, statement2):
    truth_table1 = {0: eval(statement1), 1: eval(statement1)}
    truth_table2 = {0: eval(statement2), 1: eval(statement2)}
    return truth_table1 == truth_table2

if __name__ == '__main__':
    sample_statement1 = 'x and y'
    sample_statement2 = 'y and x'
    print(are_equivalent(sample_statement1, sample_statement2))