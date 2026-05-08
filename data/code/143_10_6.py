def check_contradictory_logic(statements):
    contradictory = False
    n = len(statements)
    for i in range(n):
        for j in range(i + 1, n):
            if statements[i] == statements[j]:
                if "if" in statements[i] and "then" in statements[i]:
                    if "not" in statements[i] or "and" in statements[i] or "or" in statements[i]:
                        contradictory = True
                        break
            if contradictory:
                break
    return contradictory
if __name__ == '__main__':
    sample_statements_1 = [
        "if A then B",
        "if B then not B"
    ]
    result_1 = check_contradictory_logic(sample_statements_1)
    print(f"Sample 1 Contradictory: {result_1}")
    sample_statements_2 = [
        "if A then B",
        "if B then C"
    ]
    result_2 = check_contradictory_logic(sample_statements_2)
    print(f"Sample 2 Contradictory: {result_2}")
    sample_statements_3 = [
        "if X then Y",
        "if X then not Y"
    ]
    result_3 = check_contradictory_logic(sample_statements_3)
    print(f"Sample 3 Contradictory: {result_3}")
    sample_statements_4 = [
        "if P then Q",
        "if Q then P"
    ]
    result_4 = check_contradictory_logic(sample_statements_4)
    print(f"Sample 4 Contradictory: {result_4}")