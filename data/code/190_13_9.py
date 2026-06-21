def check_element(lst, item):
    return item in lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    target_item1 = 3
    target_item2 = 6
    print(f"Does the list contain {target_item1}? {check_element(sample_list, target_item1)}")
    print(f"Does the list contain {target_item2}? {check_element(sample_list, target_item2)}")