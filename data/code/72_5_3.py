def compare_pairs(list1, list2):
    for a, b in zip(list1, list2):
        if a > b:
            yield f'{a} > {b}'
        elif a < b:
            yield f'{a} < {b}'
        else:
            yield f'{a} == {b}'

if __name__ == '__main__':
    result = compare_pairs([1, 2, 3], [3, 2, 1])
    for comparison in result:
        print(comparison)