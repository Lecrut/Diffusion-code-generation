def check_contradictory_logic(statements):
    contradictory = False
    n = len(statements)
    for i in range(n):
        for j in range(i + 1, n):
            stmt1 = statements[i]
            stmt2 = statements[j]
            if stmt1 == stmt2:
                contradictory = True
                break
        if contradictory:
            break
    return contradictory
if __name__ == '__main__':
    sample_statements_1 = [
        "if x > 5: print('A')",
        "if x <= 5: print('B')"
    ]
    result_1 = check_contradictory_logic(sample_statements_1)
    print(f"Sample 1 Contradictory: {result_1}")
    sample_statements_2 = [
        "if a == 1: result = True",
        "if a == 1: result = False"
    ]
    result_2 = check_contradictory_logic(sample_statements_2)
    print(f"Sample 2 Contradictory: {result_2}")
    sample_statements_3 = [
        "if condition: statement_true",
        "if not condition: statement_false"
    ]
    result_3 = check_contradictory_logic(sample_statements_3)
    print(f"Sample 3 Contradictory: {result_3}")
    sample_statements_4 = [
        "if x > 0: print('Positive')",
        "if x < 0: print('Negative')"
    ]
    result_4 = check_contradictory_logic(sample_statements_4)
    print(f"Sample 4 Contradictory: {result_4}")