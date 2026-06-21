def compare_elements(lst, idx1, idx2):
    try:
        val1 = lst[idx1]
    except IndexError:
        return "index out of bounds"
    try:
        val2 = lst[idx2]
    except IndexError:
        return "index out of bounds"
    
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
    result3 = compare_elements(sample_list, 10, 2)
    print(result3)