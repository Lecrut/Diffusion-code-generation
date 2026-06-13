def compare_lists(list1, list2):
    mismatches = []
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            mismatches.append(i)
    return mismatches
if __name__ == '__main__':
    list_a = ["apple", "banana", "cherry", "date", "elderberry"]
    list_b = ["apple", "grape", "cherry", "date", "fig"]
    indices = compare_lists(list_a, list_b)
    print(indices)