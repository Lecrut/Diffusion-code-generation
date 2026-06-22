def safe_second_element(lst):
    return lst[1] if len(lst) > 1 else None

if __name__ == '__main__':
    sample_lists = {
        'list_with_two_elements': [1, 2],
        'list_with_one_element': [3],
        'empty_list': []
    }
    
    for list_name, lst in sample_lists.items():
        print(f"{list_name}: {safe_second_element(lst)}")