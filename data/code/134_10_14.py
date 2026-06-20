def check_mutual_exclusivity(set1, set2):
    return not set1.intersection(set2)

if __name__ == '__main__':
    sample_set_1 = {1, 2, 3}
    sample_set_2 = {4, 5, 6}
    print(f"Sample 1 Result: {check_mutual_exclusivity(sample_set_1, sample_set_2)}")
    
    sample_set_3 = {1, 2, 3}
    sample_set_4 = {3, 4, 5}
    print(f"Sample 2 Result: {check_mutual_exclusivity(sample_set_3, sample_set_4)}")