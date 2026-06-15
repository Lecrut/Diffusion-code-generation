def compare_lists(list1, list2):
    mismatches = []
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            mismatches.append(i)
    return mismatches
if __name__ == '__main__':
    list_a = ["apple", "banana", "cherry", "date"]
    list_b = ["apple", "orange", "cherry", "grape"]
    indices = compare_lists(list_a, list_b)
    print(indices)