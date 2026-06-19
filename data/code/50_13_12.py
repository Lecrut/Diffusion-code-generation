def symmetric_difference(set1, set2):
    return set1 ^ set2

if __name__ == '__main__':
    set_a = {10, 20, 30, 40}
    set_b = {30, 40, 50, 60}
    result_ab = symmetric_difference(set_a, set_b)
    print("Symmetric difference between set_a and set_b:", result_ab)

    set_c = {'apple', 'banana', 'cherry'}
    set_d = {'banana', 'date', 'fig'}
    result_cd = symmetric_difference(set_c, set_d)
    print("Symmetric difference between set_c and set_d:", result_cd)