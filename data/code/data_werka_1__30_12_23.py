def swap_characters(s, i, j):
    if not isinstance(s, str):
        raise TypeError('The first argument must be a string.')
    if not (isinstance(i, int) and isinstance(j, int)):
        raise TypeError('Indices must be integers.')
    if i < 0 or j < 0 or i >= len(s) or (j >= len(s)):
        raise IndexError('Index out of bounds.')
    s_list = list(s)
    s_list[i], s_list[j] = (s_list[j], s_list[i])
    return ''.join(s_list)
if __name__ == '__main__':
    sample_string = 'hello'
    index_i = 1
    index_j = 4
    try:
        result = swap_characters(sample_string, index_i, index_j)
        print(result)
    except Exception as e:
        print(e)