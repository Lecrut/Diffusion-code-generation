def union_range(list1, list2):
    combined = set(list1 + list2)
    return min(combined), max(combined)

if __name__ == '__main__':
    print(union_range([1, 3, 5], [2, 4, 6]))
    print(union_range([7, 8, 9], [9, 10, 11]))