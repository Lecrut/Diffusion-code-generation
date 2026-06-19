def validate_sets(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError("Both inputs must be sets.")

def optimized_symmetric_difference(set1, set2):
    validate_sets(set1, set2)
    return set1 ^ set2

if __name__ == '__main__':
    sample_set_a = {1, 2, 3, 4}
    sample_set_b = {3, 4, 5, 6}
    result_ab = optimized_symmetric_difference(sample_set_a, sample_set_b)
    print("Symmetric difference between sample_set_a and sample_set_b:", result_ab)

    sample_set_c = {'a', 'b', 'c'}
    sample_set_d = {'b', 'd', 'e'}
    result_cd = optimized_symmetric_difference(sample_set_c, sample_set_d)
    print("Symmetric difference between sample_set_c and sample_set_d:", result_cd)