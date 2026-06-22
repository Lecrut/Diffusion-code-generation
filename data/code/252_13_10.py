def compare_two_simple_quantities_now_rank_samples(sample_values):
    sorted_values = sorted(sample_values)
    return sorted_values

if __name__ == '__main__':
    sample1 = [5, 2, 8, 3, 7]
    result1 = compare_two_simple_quantities_now_rank_samples(sample1)
    print(result1)

    sample2 = [-1.0, -3.0, -2.5, -4.0, -1.5]
    result2 = compare_two_simple_quantities_now_rank_samples(sample2)
    print(result2)