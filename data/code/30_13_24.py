def swap_characters(s1, s2, index1, index2):
    list_s1 = list(s1)
    list_s2 = list(s2)
    list_s1[index1], list_s2[index2] = (list_s2[index2], list_s1[index1])
    swapped_s1 = ''.join(list_s1)
    swapped_s2 = ''.join(list_s2)
    return (swapped_s1, swapped_s2)
if __name__ == '__main__':
    sample_string1 = 'hello'
    sample_string2 = 'world'
    swap_index1 = 1
    swap_index2 = 4
    result1, result2 = swap_characters(sample_string1, sample_string2, swap_index1, swap_index2)
    print(result1)
    print(result2)