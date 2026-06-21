def check_item_existence(input_list, item):
    return item in set(input_list)

if __name__ == '__main__':
    my_list = [1, 5, 8, 10, 2]
    item_to_find_present = 8
    item_to_find_absent = 9
    result_present = check_item_existence(my_list, item_to_find_present)
    print(f"Is {item_to_find_present} in {my_list}? {result_present}")
    result_absent = check_item_existence(my_list, item_to_find_absent)
    print(f"Is {item_to_find_absent} in {my_list}? {result_absent}")