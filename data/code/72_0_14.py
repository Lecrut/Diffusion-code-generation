def compare_elements(list_one, list_two, target_index):
    result_one = None
    result_two = None
    length_one = len(list_one)
    length_two = len(list_two)
    if 0 <= target_index < length_one:
        result_one = list_one[target_index]
    if 0 <= target_index < length_two:
        result_two = list_two[target_index]
    return result_one, result_two

if __name__ == '__main__':
    sample_list_a = [100, 200, 300, 400]
    sample_list_b = [10, 20, 30, 40, 50]
    sample_index = 2
    val_a, val_b = compare_elements(sample_list_a, sample_list_b, sample_index)
    print((val_a, val_b))
    sample_index_out = 10
    val_c, val_d = compare_elements(sample_list_a, sample_list_b, sample_index_out)
    print((val_c, val_d))