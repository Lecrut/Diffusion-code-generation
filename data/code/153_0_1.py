def check_item_existence(item, string_list):
    if item in string_list:
        print(f"'{item}' found in the list.")
    else:
        print(f"'{item}' not found in the list.")
if __name__ == '__main__':
    target_item = "apple"
    data_list = ["banana", "orange", "apple", "grape", "kiwi"]
    check_item_existence(target_item, data_list)
    target_item = "mango"
    data_list = ["banana", "orange", "apple", "grape", "kiwi"]
    check_item_existence(target_item, data_list)