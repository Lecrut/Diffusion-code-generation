def get_first_element(lst):
    if not lst:
        return None
    return lst[0]

if __name__ == '__main__':
    sample_list = [100, 200, 300]
    empty_list = []
    
    first_element = get_first_element(sample_list)
    print(first_element)
    
    try:
        first_empty = get_first_element(empty_list)
        print(first_empty)
    except IndexError as e:
        print(e)