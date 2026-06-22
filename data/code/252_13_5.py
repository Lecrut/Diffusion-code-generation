def compare_two_simple_quantities_now_rank_samples(a, b):
    return sorted([a, b])

if __name__ == '__main__':
    sample1_a = 10.5
    sample1_b = 5.2
    result1 = compare_two_simple_quantities_now_rank_samples(sample1_a, sample1_b)
    print(result1)

    sample2_a = 3
    sample2_b = 7
    result2 = compare_two_simple_quantities_now_rank_samples(sample2_a, sample2_b)
    print(result2)

    sample3_a = -1.0
    sample3_b = -5.0
    result3 = compare_two_simple_quantities_now_rank_samples(sample3_a, sample3_b)
    print(result3)