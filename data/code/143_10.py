def check_contradictory_logic(statements):
    contradictory_pairs = []
    n = len(statements)
    for i in range(n):
        for j in range(i + 1, n):
            if statements[i] == statements[j]:
                contradictory_pairs.append((i, j))
    return contradictory_pairs
if __name__ == '__main__':
    sample_statements = [
        "A is true",
        "B is false",
        "A is false",
        "B is true",
        "A is true"
    ]
    result = check_contradictory_logic(sample_statements)
    print(result)