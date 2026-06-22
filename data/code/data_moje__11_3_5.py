def get_last_item(lst, default=None):
    if not lst:
        return default
    return lst[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    empty_list = []
    
    result1 = get_last_item(sample_list)
    result2 = get_last_item(empty_list, "No items found")
    result3 = get_last_item(empty_list, 0)
    
    print(result1)
    print(result2)
    print(result3)