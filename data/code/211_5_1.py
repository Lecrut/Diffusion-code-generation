import sys
def compare_sets(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    only_in_set1 = set1 - set2
    only_in_set2 = set2 - set1
    print("Elements present in the first set but not the second set:")
    for item in sorted(list(only_in_set1)):
        print(item)
    print("\nElements present in the second set but not the first set:")
    for item in sorted(list(only_in_set2)):
        print(item)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    compare_sets(list_a, list_b)