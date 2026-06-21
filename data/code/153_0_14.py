TARGET_ITEM = "apple"
DATA_LIST = ["banana", "orange", "apple", "grape", "kiwi"]

def check_item_existence(item, string_list):
    return item in string_list

if __name__ == '__main__':
    result = check_item_existence(TARGET_ITEM, DATA_LIST)
    print(f"'{TARGET_ITEM}' exists in the list: {result}")