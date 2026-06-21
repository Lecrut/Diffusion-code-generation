def get_final_item(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_final_item(sample_list)
    print(result)
    
    empty_list = []
    empty_result = get_final_item(empty_list)
    print(empty_result)