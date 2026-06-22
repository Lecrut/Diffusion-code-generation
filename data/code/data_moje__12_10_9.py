def get_middle_element(lst):
    if not lst:
        return None
    return lst[len(lst) // 2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_middle_element(sample_list)
    print(result)
    
    empty_list = []
    empty_result = get_middle_element(empty_list)
    print(empty_result)
    
    even_list = [1, 2, 3, 4]
    even_result = get_middle_element(even_list)
    print(even_result)