def compare_pairs(list1, list2):
    comparison_map = {
        True: '{item1} > {item2}',
        False: '{item1} < {item2}'
    }
    for item1, item2 in zip(list1, list2):
        if item1 == item2:
            yield f'{item1} == {item2}'
        else:
            result = comparison_map[item1 > item2]
            yield result.format(item1=item1, item2=item2)

if __name__ == '__main__':
    list_a = [3, 5, 7]
    list_b = [2, 4, 6]
    output = compare_pairs(list_a, list_b)
    print(list(output))