def are_equivalent(statement1, statement2):
    truth_table = {
        (True, True): eval(statement1) == eval(statement2),
        (True, False): eval(statement1) == eval(statement2),
        (False, True): eval(statement1) == eval(statement2),
        (False, False): eval(statement1) == eval(statement2)
    }
    return all(truth_table.values())

if __name__ == '__main__':
    statement1 = "a and b"
    statement2 = "b and a"
    print(are_equivalent(statement1, statement2))