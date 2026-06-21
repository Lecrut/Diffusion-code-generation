def is_subset(list1, list2):
    return set(list1).issubset(set(list2))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [1, 2, 3, 4, 5]
    sample_list3 = [1, 6]

    print(f"sample_list1 is a subset of sample_list2: {is_subset(sample_list1, sample_list2)}")
    print(f"sample_list2 is a subset of sample_list1: {is_subset(sample_list2, sample_list1)}")
    print(f"sample_list3 is a subset of sample_list1: {is_subset(sample_list3, sample_list1)}")