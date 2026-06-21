def check_item_existence(item, string_list):
    return item in string_list

if __name__ == '__main__':
    target_item = "apple"
    data_list = ["banana", "orange", "apple", "grape", "kiwi"]
    result = check_item_existence(target_item, data_list)
    print(f"'{target_item}' exists in the list: {result}")