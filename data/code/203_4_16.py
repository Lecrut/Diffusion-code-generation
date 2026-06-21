def count_greater_elements(list1, list2):
    count = 0
    for elem1, elem2 in zip(list1, list2):
        if elem1 > elem2:
            count += 1
    return count

if __name__ == '__main__':
    sample_list1 = [5, 6, 7]
    sample_list2 = [3, 4, 8]
    result = count_greater_elements(sample_list1, sample_list2)
    print(f"Count of positions where elements in {sample_list1} are greater than in {sample_list2}: {result}")