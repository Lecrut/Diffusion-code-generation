def compare_lists(list1, list2):
    results = []
    for item1, item2 in zip(list1, list2):
        try:
            if item1 == item2:
                results.append(True)
            else:
                results.append(False)
        except TypeError:
            results.append("Type Error")
    return results
if __name__ == '__main__':
    list_a = [1, 2, 'a', 4.0]
    list_b = [1, 2, 'a', 5.0]
    print(compare_lists(list_a, list_b))
    list_c = [1, 'hello', 3]
    list_d = [1, 2, 3]
    print(compare_lists(list_c, list_d))
    list_e = [1, 2, 3]
    list_f = [1, 2, 'x']
    print(compare_lists(list_e, list_f))