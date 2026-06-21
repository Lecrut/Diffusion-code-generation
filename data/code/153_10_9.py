def check_item_exists(item, data_list):
    return item in data_list

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    item1 = 3
    print(f"Does {item1} exist in {list1}? {check_item_exists(item1, list1)}")
    list2 = ['apple', 'banana', 'cherry']
    item2 = 'apple'
    print(f"Does {item2} exist in {list2}? {check_item_exists(item2, list2)}")
    list3 = [10, 20, 30]
    item3 = 5
    print(f"Does {item3} exist in {list3}? {check_item_exists(item3, list3)}")
    empty_list = []
    item4 = 'test'
    print(f"Does '{item4}' exist in an empty list? {check_item_exists(item4, empty_list)}")