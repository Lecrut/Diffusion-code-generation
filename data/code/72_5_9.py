def compare_lists(list_a, list_b):
    min_len = min(len(list_a), len(list_b))
    for i in range(min_len):
        val_a = list_a[i]
        val_b = list_b[i]
        if val_a > val_b:
            yield "A > B"
        elif val_a < val_b:
            yield "A < B"
        else:
            yield "A == B"

if __name__ == '__main__':
    list_a = [1, 5, 3, 8]
    list_b = [2, 5, 1, 9]
    results = list(compare_lists(list_a, list_b))
    print(results)