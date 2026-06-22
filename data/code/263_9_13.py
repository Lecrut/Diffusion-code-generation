def find_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4}
    sample_set2 = {3, 4, 5, 6}
    result = find_symmetric_difference(sample_set1, sample_set2)
    print(result)