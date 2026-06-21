def validate_input(item, string_list):
    if not isinstance(item, int) or not all(isinstance(i, int) for i in string_list):
        raise ValueError("Item must be an integer and the list must contain only integers.")

def check_item_existence(item, string_list):
    validate_input(item, string_list)
    return item in string_list

if __name__ == '__main__':
    target_item = 3
    data_list = [1, 2, 3, 4, 5]
    result = check_item_existence(target_item, data_list)
    if result:
        print(f"The integer {target_item} exists in the list.")
    else:
        print(f"The integer {target_item} does not exist in the list.")