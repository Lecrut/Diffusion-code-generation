def interleave_lists(list1, list2):
    result = []
    len1 = len(list1)
    len2 = len(list2)
    min_len = min(len1, len2)
    for i in range(min_len):
        result.append(list1[i])
        result.append(list2[i])
    if len1 > len2:
        result.extend(list1[min_len:])
    elif len2 > len1:
        result.extend(list2[min_len:])
    return result
if __name__ == '__main__':
    list_a = ["a", "b", "c", "d"]
    list_b = ["1", "2", "3", "4", "5"]
    interleaved = interleave_lists(list_a, list_b)
    print(interleaved)