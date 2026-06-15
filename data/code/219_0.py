def find_max(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
if __name__ == '__main__':
    sample_list1 = [1, 5, 2, 8, 3]
    sample_list2 = [-10, -5, -20, -1]
    sample_list3 = [42]
    sample_list4 = []
    print(f"Max of {sample_list1}: {find_max(sample_list1)}")
    print(f"Max of {sample_list2}: {find_max(sample_list2)}")
    print(f"Max of {sample_list3}: {find_max(sample_list3)}")
    try:
        find_max(sample_list4)
    except ValueError as e:
        print(f"Error for {sample_list4}: {e}")