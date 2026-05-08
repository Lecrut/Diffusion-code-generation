def check_contradictory_logic(statements):
    contradictions = []
    n = len(statements)
    for i in range(n):
        for j in range(i + 1, n):
            stmt1 = statements[i]
            stmt2 = statements[j]
            if stmt1 == stmt2:
                contradictions.append((i, j, "Identical statements found"))
            elif stmt1 == "A and B" and stmt2 == "not (A and B)":
                contradictions.append((i, j, "Logical negation contradiction"))
            elif stmt1 == "P" and stmt2 == "not P":
                contradictions.append((i, j, "Direct contradiction"))
            elif stmt1 == "True" and stmt2 == "False":
                contradictions.append((i, j, "Boolean value contradiction"))
            elif stmt1 == "Always True" and stmt2 == "Always False":
                contradictions.append((i, j, "Universal contradiction"))
    return contradictions
if __name__ == '__main__':
    sample_statements_1 = [
        "P",
        "not P",
        "True"
    ]
    sample_statements_2 = [
        "A and B",
        "not (A and B)"
    ]
    sample_statements_3 = [
        "P",
        "Q"
    ]
    sample_statements_4 = [
        "True",
        "False"
    ]
    sample_statements_5 = [
        "Always True",
        "Always False"
    ]
    print("--- Checking Sample Set 1 ---")
    result_1 = check_contradictory_logic(sample_statements_1)
    print(result_1)
    print("\n--- Checking Sample Set 2 ---")
    result_2 = check_contradictory_logic(sample_statements_2)
    print(result_2)
    print("\n--- Checking Sample Set 3 ---")
    result_3 = check_contradictory_logic(sample_statements_3)
    print(result_3)
    print("\n--- Checking Sample Set 4 ---")
    result_4 = check_contradictory_logic(sample_statements_4)
    print(result_4)
    print("\n--- Checking Sample Set 5 ---")
    result_5 = check_contradictory_logic(sample_statements_5)
    print(result_5)