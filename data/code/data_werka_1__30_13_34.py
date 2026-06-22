def swap_characters(s1, s2, index1, index2):
    list1 = list(s1)
    list2 = list(s2)
    list1[index1], list2[index2] = (list2[index2], list1[index1])
    swapped_s1 = ''.join(list1)
    swapped_s2 = ''.join(list2)
    return (swapped_s1, swapped_s2)
if __name__ == '__main__':
    sample_string1 = 'hello'
    sample_string2 = 'world'
    index_to_swap1 = 1
    index_to_swap2 = 4
    result1, result2 = swap_characters(sample_string1, sample_string2, index_to_swap1, index_to_swap2)
    print(result1)
    print(result2)