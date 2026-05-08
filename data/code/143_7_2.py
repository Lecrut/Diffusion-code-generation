def check_contradictions(statements):
    contradictions = []
    n = len(statements)
    for i in range(n):
        for j in range(i + 1, n):
            s1 = statements[i]
            s2 = statements[j]
            if s1 == s2:
                continue
            if ("is true" in s1 and "is false" in s2) or ("is false" in s1 and "is true" in s2):
                contradictions.append((i, j, s1, s2))
            elif ("is true" in s1 and "is false" in s2) or ("is false" in s1 and "is true" in s2):
                pass
    return contradictions
if __name__ == '__main__':
    statements = [
        "Statement 1: The sky is blue.",
        "Statement 2: The sky is not blue.",
        "Statement 3: All birds can fly.",
        "Statement 4: No birds can fly.",
        "Statement 5: 2 + 2 = 4.",
        "Statement 6: 10 is odd."
    ]
    print("--- Input Statements ---")
    for stmt in statements:
        print(stmt)
    print("\n--- Checking for Contradictions ---")
    results = check_contradictions(statements)
    if results:
        print("Contradictions Found:")
        for i, j, s1, s2 in results:
            print(f"Contradiction between Statement {i} ('{s1}') and Statement {j} ('{s2}')")
    else:
        print("No logical contradictions found based on the implemented simple check.")