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
def parse_and_check(statement_list):
    parsed_statements = []
    for stmt in statement_list:
        parts = stmt.lower().split(' is ')
        if len(parts) == 2:
            subject = parts[0].strip()
            predicate = parts[1].strip()
            parsed_statements.append({'subject': subject, 'predicate': predicate})
        else:
            parsed_statements.append({'subject': stmt, 'predicate': 'unknown'})
    contradictions = []
    n = len(parsed_statements)
    for i in range(n):
        for j in range(i + 1, n):
            p1 = parsed_statements[i]
            p2 = parsed_statements[j]
            if p1['subject'] == p2['subject']:
                if p1['predicate'] == "true" and p2['predicate'] == "false" or \
                   p1['predicate'] == "false" and p2['predicate'] == "true":
                    contradictions.append((i, j, parsed_statements[i]['subject'], parsed_statements[i]['predicate'], parsed_statements[j]['subject'], parsed_statements[j]['predicate']))
    return contradictions
if __name__ == '__main__':
    sample_statements = [
        "A is true",
        "B is true",
        "A is false",
        "B is false",
        "C is true",
        "A is true"                                
    ]
    results = parse_and_check(sample_statements)
    if results:
        print("Contradictory pairs found:")
        for i, j, s1_subj, s1_pred, s2_subj, s2_pred in results:
            print(f"Statements {i+1} and {j+1} contradict:")
            print(f"Statement {i+1}: {s1_subj} is {s1_pred}")
            print(f"Statement {j+1}: {s2_subj} is {s2_pred}")
    else:
        print("No logical contradictions found among the sample statements.")