def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

if __name__ == '__main__':
    sample_set1 = {10, 20, 30, 40}
    sample_set2 = {30, 40, 50, 60}
    result = symmetric_difference(sample_set1, sample_set2)
    print(result)