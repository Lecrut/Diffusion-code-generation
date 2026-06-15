def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return max(numbers)
if __name__ == '__main__':
    sample_list1 = [10, 5, 20, 8, 15]
    sample_list2 = [-5, -1, -10, -3]
    sample_list3 = [42]
    sample_list4 = []
    print(f"Largest in {sample_list1}: {find_largest(sample_list1)}")
    print(f"Largest in {sample_list2}: {find_largest(sample_list2)}")
    print(f"Largest in {sample_list3}: {find_largest(sample_list3)}")
    try:
        find_largest(sample_list4)
    except ValueError as e:
        print(f"Error for empty list: {e}")