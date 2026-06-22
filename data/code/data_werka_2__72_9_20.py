def compare_elements(lst, idx1, idx2):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    
    if idx1 < 0 or idx1 >= len(lst):
        raise IndexError(f"Index {idx1} is out of bounds for list of length {len(lst)}")
    
    if idx2 < 0 or idx2 >= len(lst):
        raise IndexError(f"Index {idx2} is out of bounds for list of length {len(lst)}")
    
    val1 = lst[idx1]
    val2 = lst[idx2]
    
    if val1 > val2:
        return "greater than"
    elif val1 < val2:
        return "less than"
    else:
        return "equal"

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = compare_elements(sample_list, 1, 3)
    print(result)
    
    result2 = compare_elements(sample_list, 0, 0)
    print(result2)
    
    result3 = compare_elements(sample_list, 4, 2)
    print(result3)