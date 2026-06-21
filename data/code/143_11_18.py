def check_contradictions(statements):
    n = len(statements)
    for i in range(n):
        for j in range(i + 1, n):
            if are_contradictory(statements[i], statements[j]):
                return True
    return False

def are_contradictory(s1, s2):
    s1_norm = normalize_statement(s1)
    s2_norm = normalize_statement(s2)
    return s1_norm == "~" + s2_norm or s2_norm == "~" + s1_norm

def normalize_statement(statement):
    statement = statement.lower()
    statement = statement.replace(" and ", " ").replace(" or ", " ")
    statement = statement.replace(" not ", " ~")
    return statement

if __name__ == '__main__':
    statements = ["P", "not P", "Q", "not Q"]
    print(check_contradictions(statements))