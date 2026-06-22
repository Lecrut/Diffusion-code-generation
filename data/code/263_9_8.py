def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

if __name__ == '__main__':
    set_a = {4, 5, 6, 7}
    set_b = {3, 4, 5, 8}
    result_set = symmetric_difference(set_a, set_b)
    print(result_set)