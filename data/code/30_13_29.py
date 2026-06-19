def swap_characters(s, indices):
    i, j = indices
    s_list = list(s)
    s_list[i], s_list[j] = (s_list[j], s_list[i])
    return ''.join(s_list)
if __name__ == '__main__':
    sample_string1 = 'hello'
    sample_indices1 = (0, 4)
    result1 = swap_characters(sample_string1, sample_indices1)
    print(result1)
    sample_string2 = 'world'
    sample_indices2 = (1, 3)
    result2 = swap_characters(sample_string2, sample_indices2)
    print(result2)