def check_item_existence(item, string_list):
    if item in string_list:
        print(f"'{item}' exists in the list.")
        return True
    else:
        print(f"'{item}' does not exist in the list.")
        return False
if __name__ == '__main__':
    target_item = "apple"
    data_list = ["banana", "orange", "apple", "grape", "kiwi"]
    check_item_existence(target_item, data_list)
    target_item_2 = "mango"
    data_list_2 = ["red", "green", "blue"]
    check_item_existence(target_item_2, data_list_2)