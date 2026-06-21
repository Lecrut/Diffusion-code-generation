def get_elements(lst):
    if not lst:
        return ()
    
    first = lst[0]
    last = lst[-1]
    middle_index = len(lst) // 2
    middle = lst[middle_index]
    
    return (first, middle, last)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_elements(sample_list)
    print(result)