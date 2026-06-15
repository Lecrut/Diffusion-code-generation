def compare_sets(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    diff1 = set1 - set2
    diff2 = set2 - set1
    print("Elements in the first set but not the second set:")
    for item in diff1:
        print(item)
    print("\nElements in the second set but not the first set:")
    for item in diff2:
        print(item)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    compare_sets(list_a, list_b)