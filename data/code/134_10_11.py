def check_mutual_exclusivity(set1, set2):
    return len(set1.intersection(set2)) == 0

if __name__ == '__main__':
    sample_set1 = {1, 2, 3}
    sample_set2 = {4, 5, 6}
    print(check_mutual_exclusivity(sample_set1, sample_set2))