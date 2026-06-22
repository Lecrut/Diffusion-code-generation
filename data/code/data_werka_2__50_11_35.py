def symmetric_difference(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError("Both arguments must be sets.")
    return set1 ^ set2

if __name__ == '__main__':
    SAMPLE_SET_A = {1, 2, 3, 4}
    SAMPLE_SET_B = {3, 4, 5, 6}
    SAMPLE_SET_C = {'a', 'b', 'c'}
    SAMPLE_SET_D = {'b', 'c', 'd'}

    result_ab = symmetric_difference(SAMPLE_SET_A, SAMPLE_SET_B)
    print("Symmetric difference of SAMPLE_SET_A and SAMPLE_SET_B:", result_ab)

    result_cd = symmetric_difference(SAMPLE_SET_C, SAMPLE_SET_D)
    print("Symmetric difference of SAMPLE_SET_C and SAMPLE_SET_D:", result_cd)