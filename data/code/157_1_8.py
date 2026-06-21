def find_smallest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return sorted(numbers)[0]

if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5, 9, 2]
    sample_list2 = [-10, 0, 5, -20, 3]
    sample_list3 = [7]
    empty_list = []
    
    print(f"Smallest in {sample_list1}: {find_smallest(sample_list1)}")
    print(f"Smallest in {sample_list2}: {find_smallest(sample_list2)}")
    print(f"Smallest in {sample_list3}: {find_smallest(sample_list3)}")
    try:
        find_smallest(empty_list)
    except ValueError as e:
        print(e)