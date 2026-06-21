def count_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return len(common_elements)

if __name__ == '__main__':
    list_a = ["apple", "banana", "cherry", "date"]
    list_b = ["apple", "orange", "cherry", "grape"]
    count = count_common_elements(list_a, list_b)
    print(count)