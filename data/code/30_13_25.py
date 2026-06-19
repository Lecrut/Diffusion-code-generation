def swap_characters(s1, s2, index1, index2):
    if not 0 <= index1 < len(s1) or not 0 <= index2 < len(s2):
        raise ValueError('Index out of bounds')
    list1 = list(s1)
    list2 = list(s2)
    list1[index1], list2[index2] = (list2[index2], list1[index1])
    return (''.join(list1), ''.join(list2))
if __name__ == '__main__':
    sample_string1 = 'hello'
    sample_string2 = 'world'
    swap_index1 = 1
    swap_index2 = 4
    result1, result2 = swap_characters(sample_string1, sample_string2, swap_index1, swap_index2)
    print(result1)
    print(result2)