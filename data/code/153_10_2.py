def check_item_exists(item, data_list):
    for element in data_list:
        if element == item:
            return True
    return False
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
    list4 = []
    item4 = 1
    print(f"Does {item4} exist in {list4}? {check_item_exists(item4, list4)}")
    list5 = [True, False, True]
    item5 = True
    print(f"Does {item5} exist in {list5}? {check_item_exists(item5, list5)}")
    list6 = [100, 200, 300]
    item6 = 400
    print(f"Does {item6} exist in {list6}? {check_item_exists(item6, list6)}")