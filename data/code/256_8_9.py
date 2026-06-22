def range_of_union(list1, list2):
    combined = set(list1 + list2)
    return (min(combined), max(combined))

if __name__ == '__main__':
    print(range_of_union([1, 3, 5], [2, 4, 6]))