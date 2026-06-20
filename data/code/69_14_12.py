def get_list_elements(lst):
    if not lst:
        return ()
    
    first = lst[0]
    last = lst[-1]
    length = len(lst)
    middle_index = (length - 1) // 2
    middle = lst[middle_index]
    
    return first, last, middle

if __name__ == '__main__':
    sample_list = [5, 3, 8, 1, 9, 4]
    result = get_list_elements(sample_list)
    print(result)