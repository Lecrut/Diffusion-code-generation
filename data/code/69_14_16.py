def get_list_elements(lst):
    if not lst:
        return ()
    first = lst[0]
    last = lst[-1]
    middle_index = len(lst) // 2
    middle = lst[middle_index]
    return (first, last, middle)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = get_list_elements(sample_list)
    print(result)