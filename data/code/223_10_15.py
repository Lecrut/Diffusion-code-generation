def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_list1 = [3, 9, 2, 5]
    sample_list2 = [-4, -1, -7, -2]
    sample_list3 = [10]
    empty_list = []
    
    try:
        print(f"Maximum of {sample_list1}: {find_maximum(sample_list1)}")
        print(f"Maximum of {sample_list2}: {find_maximum(sample_list2)}")
        print(f"Maximum of {sample_list3}: {find_maximum(sample_list3)}")
        find_maximum(empty_list)
    except ValueError as e:
        print(e)