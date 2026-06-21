def swap_characters(s, i, j):
    if not isinstance(s, str):
        raise TypeError('The input must be a string.')
    if not (isinstance(i, int) and isinstance(j, int)):
        raise TypeError('Indices must be integers.')
    if i < 0 or j < 0 or i >= len(s) or (j >= len(s)):
        raise IndexError('Index out of bounds.')
    char_list = list(s)
    char_list[i], char_list[j] = (char_list[j], char_list[i])
    return ''.join(char_list)
if __name__ == '__main__':
    sample_string = 'world'
    index_i = 0
    index_j = 3
    result = swap_characters(sample_string, index_i, index_j)
    print(result)