def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_list1 = [3, 5, 1, 2]
    sample_list2 = [-10, -5, -20, -1]
    sample_list3 = [42]
    empty_list = []
    
    print(f"Largest in {sample_list1}: {find_largest(sample_list1)}")
    print(f"Largest in {sample_list2}: {find_largest(sample_list2)}")
    print(f"Largest in {sample_list3}: {find_largest(sample_list3)}")
    try:
        find_largest(empty_list)
    except ValueError as e:
        print(e)