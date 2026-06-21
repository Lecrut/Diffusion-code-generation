def count_greater_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length")
    
    return sum(1 for x, y in zip(list1, list2) if x > y)

if __name__ == '__main__':
    sample_list1 = [3, 5, 7]
    sample_list2 = [2, 6, 4]
    result = count_greater_elements(sample_list1, sample_list2)
    print(f"Count of positions where elements in {sample_list1} are greater than those in {sample_list2}: {result}")