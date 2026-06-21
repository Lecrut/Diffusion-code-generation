def detect_contradictions(set1, set2):
    for var in set1:
        if var in set2:
            if set1[var] != set2[var]:
                return True
    return False

if __name__ == '__main__':
    sample_set1 = {'A': False, 'B': True}
    sample_set2 = {'A': True, 'C': False}
    print(detect_contradictions(sample_set1, sample_set2))