def check_item_existence(item, string_list):
    return item in string_list

if __name__ == '__main__':
    target_item = "apple"
    data_list = ["banana", "orange", "apple", "grape", "kiwi"]
    if check_item_existence(target_item, data_list):
        print(f"'{target_item}' exists in the list.")
    else:
        print(f"'{target_item}' does not exist in the list.")

    target_item_2 = "mango"
    data_list_2 = ["red", "green", "blue"]
    if check_item_existence(target_item_2, data_list_2):
        print(f"'{target_item_2}' exists in the list.")
    else:
        print(f"'{target_item_2}' does not exist in the list.")