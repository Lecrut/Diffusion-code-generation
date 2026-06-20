def compare_pairs(list_a, list_b):
    for a, b in zip(list_a, list_b):
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