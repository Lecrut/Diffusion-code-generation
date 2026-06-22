def intersection_without_duplicates(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

if __name__ == '__main__':
    sample_data_1 = [10, 5, 20, 8, 15]
    sample_data_2 = [-5, -1, -10, -3, 5, 15]
    print(f"Intersection: {intersection_without_duplicates(sample_data_1, sample_data_2)}")