def compare_pairs(list1, list2):
    for a in list1:
        for b in list2:
            yield (a, b)
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    comparison_iterator = compare_pairs(list_a, list_b)
    results = []
    for a, b in comparison_iterator:
        results.append((a, b))
    print(results)