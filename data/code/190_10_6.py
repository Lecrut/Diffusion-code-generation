def check_list_item(data_list, target_item):
    return target_item in data_list
if __name__ == '__main__':
    list1 = [1, 5, 10, 15, 20]
    target1 = 10
    print(f"Is {target1} in {list1}? {check_list_item(list1, target1)}")
    list2 = ['apple', 'banana', 'cherry']
    target2 = 'grape'
    print(f"Is {target2} in {list2}? {check_list_item(list2, target2)}")
    list3 = [1000, 2000, 3000]
    target3 = 1500
    print(f"Is {target3} in {list3}? {check_list_item(list3, target3)}")