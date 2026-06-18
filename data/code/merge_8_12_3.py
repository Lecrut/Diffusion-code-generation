import collections
def compare_arrays(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    symmetric_difference = set1.symmetric_difference(set2)
    return intersection, symmetric_difference
if __name__ == '__main__':
    array_a = [1, 2, 3, 4, 5, 5]
    array_b = [4, 5, 6, 7, 8, 8]
    common, diff = compare_arrays(array_a, array_b)
    print(f"Array A: {array_a}")
    print(f"Array B: {array_b}")
    print(f"Intersection (Elements present in both): {list(common)}")
    print(f"Symmetric Difference (Elements in A or B but not both): {list(diff)}")