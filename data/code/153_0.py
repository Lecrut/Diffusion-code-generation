def check_item_existence(item, string_list):
    if item in string_list:
        return True
    else:
        return False
if __name__ == '__main__':
    target_item = "apple"
    data_list = ["banana", "orange", "apple", "grape", "kiwi"]
    result = check_item_existence(target_item, data_list)
    if result:
        print(f"'{target_item}' exists in the list.")
    else:
        print(f"'{target_item}' does not exist in the list.")