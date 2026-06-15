def compare_pairs(list1, list2):
    for x in list1:
        for y in list2:
            yield (x, y)
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    comparison_iterator = compare_pairs(list_a, list_b)
    results = []
    for pair in comparison_iterator:
        results.append(pair)
    print(results)