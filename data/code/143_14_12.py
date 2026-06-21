def detect_contradictions(set1, set2):
    contradictions = []
    for var in set1:
        if var in set2:
            if set1[var] != set2[var]:
                contradictions.append((var, set1[var], set2[var]))
    return contradictions

if __name__ == '__main__':
    sample_set1 = {'A': False, 'B': True, 'C': False}
    sample_set2 = {'A': True, 'B': True, 'D': False}
    print(detect_contradictions(sample_set1, sample_set2))