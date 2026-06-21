def contains_item(data_list, item):
    return item in data_list

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    item_to_find_present = 300
    item_to_find_absent = 900
    empty_list = []
    
    result1 = contains_item(sample_list, item_to_find_present)
    print(f"Does {sample_list} contain {item_to_find_present}? {result1}")
    
    result2 = contains_item(sample_list, item_to_find_absent)
    print(f"Does {sample_list} contain {item_to_find_absent}? {result2}")
    
    result3 = contains_item(empty_list, 50)
    print(f"Does {empty_list} contain 50? {result3}")