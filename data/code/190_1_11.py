def check_item_exists(data, target):
    return target in data

if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    item1 = 5
    print(f"Does {item1} exist in the list? {check_item_exists(sample_list, item1)}")
    item2 = 9
    print(f"Does {item2} exist in the list? {check_item_exists(sample_list, item2)}")
    item3 = 2
    print(f"Does {item3} exist in the list? {check_item_exists(sample_list, item3)}")