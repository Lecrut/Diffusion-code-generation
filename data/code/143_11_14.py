def check_contradictions(statements):
    n = len(statements)
    for i in range(n):
        for j in range(i + 1, n):
            s1 = statements[i]
            s2 = statements[j]
            if are_contradictory(s1, s2):
                return True
    return False

def are_contradictory(s1, s2):
    s1_norm = s1.lower().replace(" and ", " ").replace(" or ", " ").replace(" not ", " ~")
    s2_norm = s2.lower().replace(" and ", " ").replace(" or ", " ").replace(" not ", " ~")
    return s1_norm == "~" + s2_norm or s2_norm == "~" + s1_norm

if __name__ == '__main__':
    print(check_contradictions(["P", "not P"]))