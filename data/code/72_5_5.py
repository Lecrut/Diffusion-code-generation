def compare_lists(list1, list2):
    for a, b in zip(list1, list2):
        if a > b:
            yield f'{a} > {b}'
        elif a < b:
            yield f'{a} < {b}'
        else:
            yield f'{a} == {b}'

if __name__ == '__main__':
    result = compare_lists([1, 2, 3], [4, 2, 5])
    for comparison in result:
        print(comparison)