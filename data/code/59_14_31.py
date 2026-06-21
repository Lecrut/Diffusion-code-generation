def find_middle_item(lst):
    if not lst:
        raise ValueError('The list is empty')
    
    n = len(lst)
    MIDDLE_INDEX = n // 2
    
    if n % 2 == 0:
        return (lst[MIDDLE_INDEX - 1] + lst[MIDDLE_INDEX]) / 2
    else:
        return lst[MIDDLE_INDEX]

if __name__ == '__main__':
    SAMPLE_LIST_ODD = [1, 3, 5, 7, 9]
    SAMPLE_LIST_EVEN = [2, 4, 6, 8, 10, 12]
    
    try:
        print(find_middle_item(SAMPLE_LIST_ODD))
        print(find_middle_item(SAMPLE_LIST_EVEN))
    except ValueError as e:
        print(e)