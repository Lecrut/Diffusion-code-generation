def find_first_difference(list1, list2):
    if not all((isinstance(i, (list, tuple)) for i in [list1, list2])):
        raise ValueError('Inputs must be lists or tuples')
    min_length = min(len(list1), len(list2))
    for index in range(min_length):
        if list1[index] != list2[index]:
            return index
    if len(list1) != len(list2):
        return min_length
    return -1
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [1, 2, 9, 4]
    result = find_first_difference(list_a, list_b)
    print(result)