def are_equivalent(statement1, statement2):
    truth_table1 = {i: eval(statement1) for i in range(2)}
    truth_table2 = {i: eval(statement2) for i in range(2)}
    return truth_table1 == truth_table2

if __name__ == '__main__':
    print(are_equivalent('x and y', 'y and x'))
    print(are_equivalent('not x or y', 'y or not x'))