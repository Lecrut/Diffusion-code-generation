def find_opposite_truth(value):
    lookup = {True: False, False: True}
    return lookup[value]

if __name__ == '__main__':
    val1 = True
    res1 = find_opposite_truth(val1)
    print(res1)
    val2 = False
    res2 = find_opposite_truth(val2)
    print(res2)