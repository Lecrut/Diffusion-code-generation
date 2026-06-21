def combine_lists(list_alpha, list_beta):
    combined = list_alpha.copy()
    combined.extend(list_beta)
    return combined

if __name__ == '__main__':
    sample_list_a = [1, 2, 3]
    sample_list_b = [4, 5, 6]
    result = combine_lists(sample_list_a, sample_list_b)
    print(result)