def list_operations(list1, list2, intersection=False, union=False, difference=False):
    if intersection:
        return set(list1) & set(list2)
    elif union:
        return set(list1) | set(list2)
    elif difference:
        return set(list1) - set(list2)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]

    print("Intersection:", list_operations(list1, list2, intersection=True))
    print("Union:", list_operations(list1, list2, union=True))
    print("Difference (list1 - list2):", list_operations(list1, list2, difference=True))