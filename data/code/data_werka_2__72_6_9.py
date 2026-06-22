def compare_lists(list1, list2):
    results = []
    for a, b in zip(list1, list2):
        if a < b:
            results.append(f"{a} < {b}")
        elif a > b:
            results.append(f"{a} > {b}")
        else:
            results.append(f"{a} == {b}")
    return results

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [5, 4, 3, 2, 1]
    output = compare_lists(list_a, list_b)
    for line in output:
        print(line)