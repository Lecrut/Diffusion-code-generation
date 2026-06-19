def swap_characters(s: str, indices: tuple) -> str:
    i, j = indices
    if i < 0 or j < 0 or i >= len(s) or (j >= len(s)):
        raise ValueError('Indices are out of bounds')
    s_list = list(s)
    s_list[i], s_list[j] = (s_list[j], s_list[i])
    return ''.join(s_list)
if __name__ == '__main__':
    sample_string_1 = 'hello'
    swap_indices_1 = (1, 3)
    result_1 = swap_characters(sample_string_1, swap_indices_1)
    print(result_1)
    sample_string_2 = 'world'
    swap_indices_2 = (0, 4)
    result_2 = swap_characters(sample_string_2, swap_indices_2)
    print(result_2)