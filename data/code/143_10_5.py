def check_contradictory_logic(statements):
    contradictory = False
    n = len(statements)
    for i in range(n):
        for j in range(i + 1, n):
            stmt1 = statements[i]
            stmt2 = statements[j]
            if stmt1 == stmt2:
                if "if" in stmt1 and "then" in stmt1:
                    condition1 = stmt1.split("if")[1].strip()
                    result1 = stmt1.split("then")[1].strip()
                else:
                    condition1 = stmt1
                    result1 = stmt1
                if "if" in stmt2 and "then" in stmt2:
                    condition2 = stmt2.split("if")[1].strip()
                    result2 = stmt2.split("then")[1].strip()
                else:
                    condition2 = stmt2
                    result2 = stmt2
                if condition1 == condition2 and result1 != result2:
                    contradictory = True
                    break
        if contradictory:
            break
    return contradictory
if __name__ == '__main__':
    sample_statements_1 = [
        "if x > 5 then y is true",
        "if x > 5 then y is false",
        "if x > 5 then y is true"
    ]
    sample_statements_2 = [
        "if a == 1 then b is true",
        "if a == 1 then b is false",
        "if a == 2 then b is true"
    ]
    sample_statements_3 = [
        "if condition_A then result is True",
        "if condition_A then result is False"
    ]
    sample_statements_4 = [
        "if x > 10 then result is True",
        "if x > 10 then result is True"
    ]
    sample_statements_5 = [
        "if a > 0 then result is True",
        "if a < 0 then result is True"
    ]
    print(f"Sample 1 Contradictory: {check_contradictory_logic(sample_statements_1)}")
    print(f"Sample 2 Contradictory: {check_contradictory_logic(sample_statements_2)}")
    print(f"Sample 3 Contradictory: {check_contradictory_logic(sample_statements_3)}")
    print(f"Sample 4 Contradictory: {check_contradictory_logic(sample_statements_4)}")
    print(f"Sample 5 Contradictory: {check_contradictory_logic(sample_statements_5)}")