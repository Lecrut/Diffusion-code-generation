ITEM_FOUND = True
ITEM_NOT_FOUND = False

def check_item_existence(item, string_list):
    return item in string_list

if __name__ == '__main__':
    target_item = "apple"
    data_list = ["banana", "orange", "apple", "grape", "kiwi"]
    result = check_item_existence(target_item, data_list)
    print(f"Does '{target_item}' exist in the list? {'Yes' if result else 'No'}")
    
    target_item = "mango"
    result = check_item_existence(target_item, data_list)
    print(f"Does '{target_item}' exist in the list? {'Yes' if result else 'No'}")