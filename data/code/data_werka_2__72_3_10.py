def compare_lists(list_a, list_b):
    results = []
    min_len = min(len(list_a), len(list_b))
    for i in range(min_len):
        if list_a[i] > list_b[i]:
            results.append((list_a[i], list_b[i]))
    return results

if __name__ == '__main__':
    a = [5, 3, 8, 1]
    b = [2, 4, 7, 9]
    output = compare_lists(a, b)
    print(output)