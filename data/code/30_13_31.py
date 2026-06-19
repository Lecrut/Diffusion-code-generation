def swap_characters(s: str, indices: tuple) -> str:
    i, j = indices
    if i < 0 or j < 0 or i >= len(s) or j >= len(s):
        raise ValueError("Indices are out of bounds")
    s_list = list(s)
    s_list[i], s_list[j] = s_list[j], s_list[i]
    return ''.join(s_list)

if __name__ == '__main__':
    sample_string = "hello world"
    swap_indices = (1, 7)
    result = swap_characters(sample_string, swap_indices)
    print(result)