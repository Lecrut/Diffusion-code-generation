def swap_characters(s1, s2, index1, index2):
    if index1 < 0 or index1 >= len(s1) or index2 < 0 or (index2 >= len(s2)):
        raise ValueError('Indices out of bounds')
    s1_list = list(s1)
    s2_list = list(s2)
    s1_list[index1], s2_list[index2] = (s2_list[index2], s1_list[index1])
    return (''.join(s1_list), ''.join(s2_list))
if __name__ == '__main__':
    sample_string1 = 'hello'
    sample_string2 = 'world'
    swap_index1 = 1
    swap_index2 = 3
    result1, result2 = swap_characters(sample_string1, sample_string2, swap_index1, swap_index2)
    print(result1)
    print(result2)