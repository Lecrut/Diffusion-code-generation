def check_contradictions(statements):
    contradictions = []
    n = len(statements)
    for i in range(n):
        for j in range(i + 1, n):
            s1 = statements[i]
            s2 = statements[j]
            if s1 == s2:
                continue
            pass                                
    return contradictions
def find_contradictory_pairs(statements):
    contradictions = []
    n = len(statements)
    for i in range(n):
        for j in range(i + 1, n):
            s1 = statements[i]
            s2 = statements[j]
            pass
    contradictions = []
    for i in range(len(statements)):
        for j in range(i + 1, len(statements)):
            s1, s2 = statements[i], statements[j]
            if s1 == f"NOT({s2})" or s2 == f"NOT({s1})":
                contradictions.append((s1, s2))
    return contradictions
if __name__ == '__main__':
    sample_statements = [
        "P",
        "Q",
        "NOT(P)",
        "NOT(Q)",
        "P",                                               
        "NOT(P)"                              
    ]
    contradictory_pairs = find_contradictory_pairs(sample_statements)
    if contradictory_pairs:
        print("Contradictory pairs found:")
        for s1, s2 in contradictory_pairs:
            print(f"Statement 1: {s1}, Statement 2: {s2}")
    else:
        print("No logical contradictions found in the sample set.")