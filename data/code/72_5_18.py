def compare_pairs(list1, list2):
    for item1, item2 in zip(list1, list2):
        if item1 > item2:
            yield f'{item1} > {item2}'
        elif item1 < item2:
            yield f'{item1} < {item2}'
        else:
            yield f'{item1} == {item2}'

if __name__ == '__main__':
    list_a = [3, 5, 7]
    list_b = [2, 4, 6]
    output = compare_pairs(list_a, list_b)
    for comparison in output:
        print(comparison)