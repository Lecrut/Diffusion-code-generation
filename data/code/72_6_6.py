def compare_lists(list1, list2):
    return [f'{x} == {y}' if x == y else f'{x} > {y}' if x > y else f'{x} < {y}' for x, y in zip(list1, list2)]
if __name__ == '__main__':
    list_a = [1, 5, 10, 15]
    list_b = [2, 4, 10, 20]
    results = compare_lists(list_a, list_b)
    for result in results:
        print(result)