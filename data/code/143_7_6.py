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
            s1 = statements[i].lower().strip()
            s2 = statements[j].lower().strip()
            if (s1 == "P" and s2 == "not P") or (s1 == "not P" and s2 == "P"):
                contradictions.append((s1, s2))
            elif (s1 == "A" and s2 == "not A") or (s1 == "not A" and s2 == "A"):
                contradictions.append((s1, s2))
            elif (s1 == "Q" and s2 == "not Q") or (s1 == "not Q" and s2 == "Q"):
                contradictions.append((s1, s2))
    return contradictions
if __name__ == '__main__':
    sample_statements = [
        "P",
        "Q",
        "not P",
        "not Q",
        "P",
        "not Q"
    ]
    contradictory_pairs = check_logical_contradictions(sample_statements)
    if contradictory_pairs:
        print("Contradictions found:")
        for s1, s2 in contradictory_pairs:
            print(f"Statement 1: {s1} and Statement 2: {s2} are contradictory.")
    else:
        print("No logical contradictions found based on the defined rules.")