def check_integer_exists(integer_list, target):
    integer_set = set(integer_list)
    return target in integer_set

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    item_to_check_present = 30
    item_to_check_absent = 60
    
    result_present = check_integer_exists(sample_list, item_to_check_present)
    print(f"Is {item_to_check_present} in {sample_list}? {result_present}")
    
    result_absent = check_integer_exists(sample_list, item_to_check_absent)
    print(f"Is {item_to_check_absent} in {sample_list}? {result_absent}")