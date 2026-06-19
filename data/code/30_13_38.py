def swap_characters(s1, s2, index1, index2):
    list1 = list(s1)
    list2 = list(s2)
    list1[index1], list2[index2] = (list2[index2], list1[index1])
    swapped_s1 = ''.join(list1)
    swapped_s2 = ''.join(list2)
    return (swapped_s1, swapped_s2)
if __name__ == '__main__':
    string1 = 'hello'
    string2 = 'world'
    index1 = 1
    index2 = 4
    result = swap_characters(string1, string2, index1, index2)
    print(result)