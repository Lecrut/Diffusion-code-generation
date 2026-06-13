def check_membership(items, target):
    return target in items
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    target_item = 30
    result = check_membership(sample_list, target_item)
    print(f"List: {sample_list}")
    print(f"Target: {target_item}")
    print(f"Is {target_item} in the list? {result}")
    sample_list_2 = ['apple', 'banana', 'cherry']
    target_item_2 = 'apple'
    result_2 = check_membership(sample_list_2, target_item_2)
    print(f"\nList: {sample_list_2}")
    print(f"Target: {target_item_2}")
    print(f"Is {target_item_2} in the list? {result_2}")