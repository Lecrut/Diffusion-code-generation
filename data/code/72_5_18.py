def compare_lists(list_a, list_b):
    min_len = min(len(list_a), len(list_b))
    for i in range(min_len):
        val_a = list_a[i]
        val_b = list_b[i]
        if val_a > val_b:
            yield f'{val_a} > {val_b}'
        elif val_a < val_b:
            yield f'{val_a} < {val_b}'
        else:
            yield f'{val_a} == {val_b}'

if __name__ == '__main__':
    list_a = [1, 5, 3, 8]
    list_b = [2, 5, 1, 8, 9]
    results = list(compare_lists(list_a, list_b))
    print(results)