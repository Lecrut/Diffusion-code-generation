def check_list_item(input_list, item):
    return item in set(input_list)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    search_item_present = 30
    search_item_absent = 60
    
    result_present = check_list_item(sample_list, search_item_present)
    print(f"Is {search_item_present} in {sample_list}? {result_present}")
    
    result_absent = check_list_item(sample_list, search_item_absent)
    print(f"Is {search_item_absent} in {sample_list}? {result_absent}")