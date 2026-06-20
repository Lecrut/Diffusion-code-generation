def check_mutual_exclusivity(set1, set2):
    intersection = set1.intersection(set2)
    return len(intersection) == 0

if __name__ == '__main__':
    sample_set_1 = {1, 2, 3}
    sample_set_2 = {4, 5, 6}
    result1 = check_mutual_exclusivity(sample_set_1, sample_set_2)
    print(f"Result 1: {result1}")

    sample_set_3 = {1, 2, 3}
    sample_set_4 = {3, 4, 5}
    result2 = check_mutual_exclusivity(sample_set_3, sample_set_4)
    print(f"Result 2: {result2}")