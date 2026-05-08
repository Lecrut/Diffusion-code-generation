def compare_list_sizes(list1, list2):
    size1 = len(list1)
    size2 = len(list2)
    if size1 > size2:
        return f"List 1 is larger. Size of List 1: {size1}, Size of List 2: {size2}"
    elif size2 > size1:
        return f"List 2 is larger. Size of List 1: {size1}, Size of List 2: {size2}"
    else:
        return f"Both lists have the same size. Size: {size1}"
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [10, 20, 30]
    result = compare_list_sizes(list_a, list_b)
    print(result)