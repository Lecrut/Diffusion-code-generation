def symmetric_difference(set_a, set_b):
    return set_a.symmetric_difference(set_b)

if __name__ == '__main__':
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    result = symmetric_difference(set1, set2)
    print(result)