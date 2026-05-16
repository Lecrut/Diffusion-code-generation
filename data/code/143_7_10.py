def check_contradictions(statements):
    contradictions = []
    n = len(statements)
    for i in range(n):
        for j in range(i + 1, n):
            stmt1 = statements[i]
            stmt2 = statements[j]
            if stmt1 == stmt2:
                continue
            if (stmt1 == "P" and stmt2 == "not P") or \
               (stmt1 == "not P" and stmt2 == "P"):
                contradictions.append((i, j, "Direct Negation"))
            elif (stmt1 == "A and B" and stmt2 == "not (A and B)"):
                pass
    return contradictions
if __name__ == '__main__':
    statements_list = [
        "P",
        "not P",
        "Q",
        "not Q",
        "P and Q",
        "not (P and Q)"
    ]
    print("Statements provided:")
    for i, stmt in enumerate(statements_list):
        print(f"Statement {i}: {stmt}")
    contradictions_found = check_contradictions(statements_list)
    if contradictions_found:
        print("\nContradictions Found:")
        for i, j, reason in contradictions_found:
            print(f"Statements at indices {i} and {j} are contradictory. Reason: {reason}")
    else:
        print("\nNo direct logical contradictions found based on the implemented rules.")