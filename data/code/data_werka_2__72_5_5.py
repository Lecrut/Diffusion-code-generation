def compare_lists(list_a, list_b):
    min_len = min(len(list_a), len(list_b))
    for i in range(min_len):
        a = list_a[i]
        b = list_b[i]
        if a > b:
            yield 'A > B'
        elif a < b:
            yield 'A < B'
        else:
            yield 'A == B'

if __name__ == '__main__':
    list_a = [1, 5, 3, 8]
    list_b = [2, 5, 2, 9, 10]
    results = list(compare_lists(list_a, list_b))
    print(results)