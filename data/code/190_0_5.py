def check_list_item(input_list, item):
    return item in input_list
if __name__ == '__main__':
    my_list = [1, 5, 2, 8, 3]
    item_to_find_present = 8
    item_to_find_absent = 9
    result1 = check_list_item(my_list, item_to_find_present)
    print(f"Is {item_to_find_present} in {my_list}? {result1}")
    result2 = check_list_item(my_list, item_to_find_absent)
    print(f"Is {item_to_find_absent} in {my_list}? {result2}")