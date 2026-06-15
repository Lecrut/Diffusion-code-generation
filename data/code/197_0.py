def check_membership(items, target):
    return target in items
if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    item_to_check = 30
    result = check_membership(my_list, item_to_check)
    print(f"List: {my_list}")
    print(f"Checking for item: {item_to_check}")
    print(f"Is {item_to_check} in the list? {result}")
    my_list_2 = ['apple', 'banana', 'cherry']
    item_to_check_2 = 'apple'
    result_2 = check_membership(my_list_2, item_to_check_2)
    print(f"\nList: {my_list_2}")
    print(f"Checking for item: {item_to_check_2}")
    print(f"Is {item_to_check_2} in the list? {result_2}")