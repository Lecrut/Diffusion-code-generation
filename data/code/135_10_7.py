def are_equivalent(statement1, statement2):
    truth_table = []
    for a in [True, False]:
        for b in [True, False]:
            truth_table.append((a, b, eval(statement1) == eval(statement2)))
    return truth_table

if __name__ == '__main__':
    statement1 = "a and b"
    statement2 = "b and a"
    print(are_equivalent(statement1, statement2))