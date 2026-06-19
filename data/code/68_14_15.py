def symmetric_difference(iterable1, iterable2):
    set1 = set(iterable1)
    set2 = set(iterable2)
    return list(set1.symmetric_difference(set2))

if __name__ == '__main__':
    sample_list_a = [3, 7, 9, 10]
    sample_list_b = [5, 7, 10, 12]
    result = symmetric_difference(sample_list_a, sample_list_b)
    print(result)