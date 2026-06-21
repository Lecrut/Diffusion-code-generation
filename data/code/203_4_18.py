def count_greater_elements(list1, list2):
    if not all(isinstance(i, (int, float)) for i in list1 + list2) or len(list1) != len(list2):
        raise ValueError("Both lists must contain only numbers and be of equal length.")
    
    return sum(1 for a, b in zip(list1, list2) if a > b)

if __name__ == '__main__':
    sample_list1 = [3, 5, 7, 9]
    sample_list2 = [1, 4, 6, 8]
    result = count_greater_elements(sample_list1, sample_list2)
    print(f"Count of positions where elements in {sample_list1} are greater than in {sample_list2}: {result}")