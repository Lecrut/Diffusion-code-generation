def detect_contradictions(set1, set2):
    contradictions = []
    for var, val1 in set1.items():
        if var in set2 and set2[var] != val1:
            contradictions.append((var, val1, set2[var]))
    return contradictions
if __name__ == '__main__':
    sample_set1 = {'A': True, 'B': False, 'C': True}
    sample_set2 = {'A': True, 'B': True, 'D': False}
    result = detect_contradictions(sample_set1, sample_set2)
    print(result)