def is_contradictory(s1, s2):
    s1_lower = s1.lower().replace(" ", "")
    s2_lower = s2.lower().replace(" ", "")
    if s1_lower == s2_lower:
        return False
    if s1_lower.startswith("not") and s2_lower.replace("not", "") == s1_lower[3:]:
        return True
    if s2_lower.startswith("not") and s1_lower.replace("not", "") == s2_lower[3:]:
        return True
    return False

def check_contradictions(statements):
    n = len(statements)
    for i in range(n):
        for j in range(i + 1, n):
            if is_contradictory(statements[i], statements[j]):
                return True
    return False

if __name__ == '__main__':
    sample_statements = ["P", "not P", "A", "not A", "B and C", "not B or not C"]
    print(check_contradictions(sample_statements))