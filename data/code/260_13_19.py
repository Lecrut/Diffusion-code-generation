def is_subset(subset, superset):
    return set(subset).issubset(superset)
if __name__ == '__main__':
    sample_subset = [1, 2]
    sample_superset = [1, 2, 3, 4]
    print(is_subset(sample_subset, sample_superset))
    sample_subset = [5, 6]
    sample_superset = [1, 2, 3, 4]
    print(is_subset(sample_subset, sample_superset))