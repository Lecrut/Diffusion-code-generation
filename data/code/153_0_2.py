def check_item_existence(item_to_find, string_list):
    if item_to_find in string_list:
        return True
    else:
        return False
if __name__ == '__main__':
    target_item = "apple"
    data_list = ["banana", "orange", "apple", "grape", "kiwi"]
    result = check_item_existence(target_item, data_list)
    print(f"Does '{target_item}' exist in the list? {result}")
    target_item_2 = "mango"
    data_list_2 = ["banana", "orange", "apple", "grape", "kiwi"]
    result_2 = check_item_existence(target_item_2, data_list_2)
    print(f"Does '{target_item_2}' exist in the list? {result_2}")