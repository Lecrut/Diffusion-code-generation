def union_range(list1, list2):
    combined = set(list1 + list2)
    return (min(combined), max(combined))

if __name__ == '__main__':
    sample_list1 = [10, 5, 3, 8]
    sample_list2 = [7, 9, 5, 1]
    print(union_range(sample_list1, sample_list2))