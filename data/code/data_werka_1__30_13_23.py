def swap_characters(s: str, indices: tuple) -> str:
    i, j = indices
    if i < 0 or j < 0 or i >= len(s) or (j >= len(s)):
        raise ValueError('Indices are out of bounds')
    s_list = list(s)
    s_list[i], s_list[j] = (s_list[j], s_list[i])
    return ''.join(s_list)
if __name__ == '__main__':
    sample_string1 = 'hello'
    swap_indices1 = (1, 3)
    result1 = swap_characters(sample_string1, swap_indices1)
    print(result1)
    sample_string2 = 'world'
    swap_indices2 = (0, 4)
    result2 = swap_characters(sample_string2, swap_indices2)
    print(result2)