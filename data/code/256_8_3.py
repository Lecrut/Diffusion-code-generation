def union_range(list1, list2):
    combined = set(list1 + list2)
    return (min(combined), max(combined))

if __name__ == '__main__':
    sample_list1 = [3, 5, 7, 9]
    sample_list2 = [2, 4, 6, 8, 9]
    print(union_range(sample_list1, sample_list2))