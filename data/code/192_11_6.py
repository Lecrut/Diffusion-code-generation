def find_common_elements(seq1, seq2):
    set_a = set(seq1)
    set_b = set(seq2)
    common_elements = set_a & set_b
    return list(common_elements)

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50, 60, 70, 80]
    sample_list2 = [30, 40, 50, 90, 100, 10]
    result = find_common_elements(sample_list1, sample_list2)
    print(result)