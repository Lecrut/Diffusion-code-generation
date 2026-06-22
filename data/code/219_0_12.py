def find_max(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return max(numbers)

if __name__ == '__main__':
    sample_list1 = [3, 7, 2, 5, 9]
    sample_list2 = [-4, -2, -8, -6, -1]
    sample_list3 = [0]
    print(f"Max of {sample_list1}: {find_max(sample_list1)}")
    print(f"Max of {sample_list2}: {find_max(sample_list2)}")
    print(f"Max of {sample_list3}: {find_max(sample_list3)}")