def find_larger_set(set1, set2):
    if len(set1) > len(set2):
        return set1
    elif len(set2) > len(set1):
        return set2
    else:
        return set1 if set1 != set2 else None

if __name__ == '__main__':
    sample_set_1 = {1, 2, 3}
    sample_set_2 = {4, 5, 6, 7}
    larger_set = find_larger_set(sample_set_1, sample_set_2)
    print(larger_set)