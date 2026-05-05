def compare_lists(list1, list2):
    for item1, item2 in zip(list1, list2):
        if item1 > item2:
            yield f"{item1} > {item2}"
        elif item1 < item2:
            yield f"{item1} < {item2}"
        else:
            yield f"{item1} == {item2}"
if __name__ == '__main__':
    list_a = [1, 5, 10, 15]
    list_b = [2, 4, 10, 20]
    results = list(compare_lists(list_a, list_b))
    for result in results:
        print(result)