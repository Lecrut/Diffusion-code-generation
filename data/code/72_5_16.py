def compare_pairs(list1, list2):
    comparison_map = {
        True: '{} > {}',
        False: '{} < {}'
    }
    for item1, item2 in zip(list1, list2):
        if item1 == item2:
            yield f'{item1} == {item2}'
        else:
            result = comparison_map[item1 > item2].format(item1, item2)
            yield result

if __name__ == '__main__':
    list_a = [3, 5, 7]
    list_b = [2, 4, 6]
    output = compare_pairs(list_a, list_b)
    print(list(output))