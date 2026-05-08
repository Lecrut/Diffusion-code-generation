def symmetric_difference(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return set_a.symmetric_difference(set_b)
if __name__ == '__main__':
    list_a_sample = [1, 2, 3, 4, 5]
    list_b_sample = [4, 5, 6, 7, 8]
    result = symmetric_difference(list_a_sample, list_b_sample)
    print(result)