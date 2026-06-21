def is_subset(subset, master):
    return all(item in master for item in subset)

if __name__ == '__main__':
    sample_subset = [1, 2, 3]
    sample_master = [1, 2, 3, 4, 5]
    print(is_subset(sample_subset, sample_master))