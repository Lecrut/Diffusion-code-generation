def evaluate_condition(condition_string):
    if not condition_string:
        return False
    parts = condition_string.lower().split()
    if len(parts) == 0:
        return False
    results = {}
    for part in parts:
        if 'and' in part:
            continue
        if 'or' in part:
            continue
        if part in ['and', 'or']:
            continue
        if part.isalpha() and 'a' <= part[0] <= 'z':
            try:
                results[part] = True
            except Exception:
                results[part] = False
        else:
            results[part] = False
    if not results:
        return False
    if 'and' in condition_string:
        and_clauses = condition_string.split('and')
        all_true = True
        for clause in and_clauses:
            clause = clause.strip()
            if not clause:
                continue
            sub_parts = clause.split()
            if not sub_parts:
                continue
            clause_result = True
            for sub_part in sub_parts:
                if sub_part.isalpha() and 'a' <= sub_part[0] <= 'z':
                    if not results.get(sub_part, False):
                        clause_result = False
                        break
                else:
                    clause_result = False
                    break
            if not clause_result:
                all_true = False
                break
        return all_true
    elif 'or' in condition_string:
        or_clauses = condition_string.split('or')
        any_true = False
        for clause in or_clauses:
            clause = clause.strip()
            if not clause:
                continue
            sub_parts = clause.split()
            if not sub_parts:
                continue
            clause_result = False
            for sub_part in sub_parts:
                if sub_part.isalpha() and 'a' <= sub_part[0] <= 'z':
                    if results.get(sub_part, False):
                        clause_result = True
                        break
                else:
                    clause_result = False
                    break
            if clause_result:
                any_true = True
                break
        return any_true
    else:
        if len(parts) >= 2:
            return all(results.get(part, False) for part in parts if part.isalpha())
        return False
if __name__ == '__main__':
    test_cases = [
        ("A and B", True),
        ("A and not B", False),
        ("A or B", True),
        ("not A and B", False),
        ("A or B or C", True),
        ("A and B and C", False),
        ("A and B and C", True),
        ("A and B and not C", False),
        ("A and B and C", True),
        ("A and B", True),
        ("B or C", True),
        ("A and B", False),
        ("A and B and C", True),
        ("A or B", True),
        ("A and B", False),
        ("A and B and C", True),
        ("A or B", True),
        ("A and B", False),
        ("A and B and C", True),
        ("A or B", True),
    ]
    for input_str, expected in test_cases:
        actual = evaluate_condition(input_str)
        print(f"Input: '{input_str}', Expected: {expected}, Actual: {actual}, Match: {actual == expected}")