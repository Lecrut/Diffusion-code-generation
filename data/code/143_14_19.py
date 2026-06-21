def detect_contradictions(set1, set2):
    contradictions = []
    for var in set1:
        if var in set2:
            val1 = set1[var]
            val2 = set2[var]
            if val1 != val2:
                contradictions.append((var, val1, val2))
    return contradictions
if __name__ == '__main__':
    sample_set1 = {'A': True, 'B': False, 'C': True}
    sample_set2 = {'A': True, 'B': True, 'D': False}
    result = detect_contradictions(sample_set1, sample_set2)
    print(result)