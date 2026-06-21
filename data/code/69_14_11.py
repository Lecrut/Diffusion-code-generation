def get_elements(lst):
    if not lst:
        return ()
    
    first = lst[0]
    last = lst[-1]
    middle = lst[len(lst) // 2] if len(lst) > 1 else first
    
    return first, middle, last

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_elements(sample_list)
    print(result)

    empty_list = []
    result_empty = get_elements(empty_list)
    print(result_empty)