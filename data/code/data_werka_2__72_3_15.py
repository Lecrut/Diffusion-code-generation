def compare_lists(list_a, list_b):
    results = []
    min_len = min(len(list_a), len(list_b))
    for i in range(min_len):
        if list_a[i] > list_b[i]:
            results.append((list_a[i], list_b[i]))
    return results

if __name__ == '__main__':
    list_a = [5, 3, 8, 2]
    list_b = [4, 6, 7, 1]
    result = compare_lists(list_a, list_b)
    for pair in result:
        print(f"{pair[0]} > {pair[1]}")