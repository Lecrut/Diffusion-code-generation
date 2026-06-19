def calculate_symmetric_difference(set1, set2):
    return set1 ^ set2

if __name__ == '__main__':
    sample_set_a = {1, 3, 5, 7}
    sample_set_b = {2, 3, 6, 8}
    result_ab = calculate_symmetric_difference(sample_set_a, sample_set_b)
    print("Symmetric difference between sample_set_a and sample_set_b:", result_ab)

    sample_set_c = {'apple', 'banana', 'cherry'}
    sample_set_d = {'banana', 'dragonfruit', 'elderberry'}
    result_cd = calculate_symmetric_difference(sample_set_c, sample_set_d)
    print("Symmetric difference between sample_set_c and sample_set_d:", result_cd)