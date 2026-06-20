def compare_pairs(list1, list2):
    for a, b in zip(list1, list2):
        if a > b:
            yield f'{a} > {b}'
        elif a < b:
            yield f'{a} < {b}'
        else:
            yield f'{a} == {b}'

if __name__ == '__main__':
    list_a = [3, 5, 7]
    list_b = [2, 4, 6]
    output = compare_pairs(list_a, list_b)
    print(list(output))