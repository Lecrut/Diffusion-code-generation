def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum

if __name__ == '__main__':
    sample_list1 = [5, 2, 8, 1, 9]
    sample_list2 = [-10, 0, 50, -3]
    empty_list = []
    
    print(f"Minimum of {sample_list1}: {find_minimum(sample_list1)}")
    print(f"Minimum of {sample_list2}: {find_minimum(sample_list2)}")
    try:
        find_minimum(empty_list)
    except ValueError as e:
        print(e)