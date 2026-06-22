def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = [-5, -10, -15, -20, -25]
    empty_list = []
    
    print(f"Maximum of {sample_list1}: {find_maximum(sample_list1)}")
    print(f"Maximum of {sample_list2}: {find_maximum(sample_list2)}")
    try:
        find_maximum(empty_list)
    except ValueError as e:
        print(e)