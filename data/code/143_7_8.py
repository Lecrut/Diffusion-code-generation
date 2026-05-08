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
def check_logical_contradictions(statements):
    contradictions = []
    n = len(statements)
    for i in range(n):
        for j in range(i + 1, n):
            s1 = statements[i]
            s2 = statements[j]
            if (s1 == "P") and (s2 == "not P"):
                contradictions.append((i, j, "P and not P"))
            elif (s1 == "Q") and (s2 == "not Q"):
                contradictions.append((i, j, "Q and not Q"))
            elif (s1 == "R") and (s2 == "not R"):
                contradictions.append((i, j, "R and not R"))
    return contradictions
if __name__ == '__main__':
    sample_statements = [
        "P",
        "Q",
        "R",
        "not P",
        "not Q",
        "not R",
        "P",                                       
        "Q"
    ]
    results = check_logical_contradictions(sample_statements)
    if results:
        print("Contradictions found:")
        for i, j, reason in results:
            print(f"Statements at index {i} ('{sample_statements[i]}' and index {j} ('{sample_statements[j]}')) are contradictory: {reason}")
    else:
        print("No logical contradictions found in the sample set.")