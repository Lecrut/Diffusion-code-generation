def find_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5, 9, 2]
    sample_list2 = [-10, -5, -20, -1]
    sample_list3 = [7]
    sample_list4 = []
    
    print(f"Max of {sample_list1}: {find_max(sample_list1)}")
    print(f"Max of {sample_list2}: {find_max(sample_list2)}")
    print(f"Max of {sample_list3}: {find_max(sample_list3)}")