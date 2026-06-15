import sys
def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common = set1.intersection(set2)
    return list(common)
if __name__ == '__main__':
    list_a = list(range(1000000))
    list_b = list(range(500000, 1500001))
    common_elements = find_common_elements(list_a, list_b)
    print(f"Number of common elements found: {len(common_elements)}")
    print("First 10 common elements:")
    for i in range(min(10, len(common_elements))):
        print(common_elements[i])
    if len(common_elements) > 10:
        print("...")