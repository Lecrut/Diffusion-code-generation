def swap_characters(s, indices):
    i, j = indices
    s_list = list(s)
    s_list[i], s_list[j] = (s_list[j], s_list[i])
    return ''.join(s_list)
if __name__ == '__main__':
    sample_string_1 = 'hello'
    sample_indices_1 = (0, 4)
    result_1 = swap_characters(sample_string_1, sample_indices_1)
    sample_string_2 = 'world'
    sample_indices_2 = (1, 3)
    result_2 = swap_characters(sample_string_2, sample_indices_2)
    print(result_1)
    print(result_2)