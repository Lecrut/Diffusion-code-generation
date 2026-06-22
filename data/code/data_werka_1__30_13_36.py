def swap_characters(s: str, index1: int, index2: int) -> str:
    if not 0 <= index1 < len(s) or not 0 <= index2 < len(s):
        raise ValueError('Indices are out of bounds')
    s_list = list(s)
    s_list[index1], s_list[index2] = (s_list[index2], s_list[index1])
    return ''.join(s_list)
if __name__ == '__main__':
    sample_string = 'hello'
    index1 = 1
    index2 = 3
    result = swap_characters(sample_string, index1, index2)
    print(result)