def truth_table_results(bool_list1, bool_list2):
    if len(bool_list1) != len(bool_list2):
        raise ValueError("Both lists must have the same length")

    results = []
    for a, b in zip(bool_list1, bool_list2):
        and_result = a and b
        or_result = a or b
        xor_result = a ^ b
        results.append((a, b, and_result, or_result, xor_result))

    return results

if __name__ == '__main__':
    sample_values = [True, False, True]
    print(truth_table_results(sample_values, sample_values))