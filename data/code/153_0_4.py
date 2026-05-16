def check_item_existence(item_to_find, string_list):
    if item_to_find in string_list:
        print(f"'{item_to_find}' was found in the list.")
    else:
        print(f"'{item_to_find}' was not found in the list.")
if __name__ == '__main__':
    target_item = "apple"
    data_list = ["banana", "orange", "apple", "grape", "kiwi"]
    check_item_existence(target_item, data_list)