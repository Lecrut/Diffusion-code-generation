def compare_lists(list1, list2):
    results = []
    for a, b in zip(list1, list2):
        if a > b:
            results.append(1)
        elif a < b:
            results.append(-1)
        else:
            results.append(0)
    return results

if __name__ == '__main__':
    list_a = [1, 5, 3, 8]
    list_b = [2, 4, 3, 8]
    print(compare_lists(list_a, list_b))