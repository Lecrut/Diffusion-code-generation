def compare_elements(lst, idx1, idx2):
    if idx1 < 0 or idx1 >= len(lst) or idx2 < 0 or idx2 >= len(lst):
        raise IndexError("Index out of bounds")
    
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