def interleave_lists(list1, list2):
    result = []
    for i in range(min(len(list1), len(list2))):
        result.append(list1[i])
        result.append(list2[i])
    return result
if __name__ == '__main__':
    list_a = ["a", "b", "c", "d"]
    list_b = ["1", "2", "3", "4", "5"]
    interleaved = interleave_lists(list_a, list_b)
    print(interleaved)