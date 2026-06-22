def symmetric_difference(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError("Both arguments must be sets.")
    return set1 ^ set2

if __name__ == '__main__':
    try:
        set_a = {1, 2, 3, 4}
        set_b = {3, 4, 5, 6}
        result_ab = symmetric_difference(set_a, set_b)
        print(result_ab)

        set_c = {'a', 'b', 'c'}
        set_d = {'b', 'c', 'd'}
        result_cd = symmetric_difference(set_c, set_d)
        print(result_cd)
    except ValueError as e:
        print(e)