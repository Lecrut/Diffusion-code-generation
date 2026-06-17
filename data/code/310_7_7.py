def interleave_lists(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    max_len = max(len1, len2)
    result = []
    for i in range(max_len):
        if i < len1:
            result.append(list1[i])
        if i < len2:
            result.append(list2[i])
    return result
if __name__ == '__main__':
    list_a = ["a1", "a2", "a3", "a4"]
    list_b = ["b1", "b2", "b3", "b4", "b5"]
    interleaved = interleave_lists(list_a, list_b)
    print(" ".join(interleaved))