def filter_greater_elements(set1, set2):
    greater_set = [x for x in set1 if x > max(set2)] + [y for y in set2 if y > max(set1)]
    return greater_set

if __name__ == '__main__':
    sample_set1 = {10, 20, 30, 40}
    sample_set2 = {5, 15, 25, 35}
    result = filter_greater_elements(sample_set1, sample_set2)
    print(result)