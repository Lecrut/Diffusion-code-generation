def compare_lists(list1, list2):
    results = []
    for i in range(min(len(list1), len(list2))):
        if list1[i] > list2[i]:
            results.append((list1[i], list2[i]))
    return results

if __name__ == '__main__':
    a = [5, 3, 8, 1]
    b = [2, 4, 7, 2]
    print(compare_lists(a, b))