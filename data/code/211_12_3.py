def set_difference_sorted(sample1, sample2):
    set1 = set(sample1)
    set2 = set(sample2)
    difference = set1 - set2
    return sorted(list(difference))
if __name__ == '__main__':
    sample1 = [1, 5, 2, 8, 3, 5]
    sample2 = [5, 9, 2, 4, 1]
    result = set_difference_sorted(sample1, sample2)
    print(result)