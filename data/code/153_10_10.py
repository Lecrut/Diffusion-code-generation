def check_item_exists(item, data_list):
    return item in data_list

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    item1 = 3
    result1 = check_item_exists(item1, list1)
    print(f"Does {item1} exist in {list1}? {result1}")

    list2 = ['apple', 'banana', 'cherry']
    item2 = 'grape'
    result2 = check_item_exists(item2, list2)
    print(f"Does {item2} exist in {list2}? {result2}")

    list3 = [True, False, True]
    item3 = True
    result3 = check_item_exists(item3, list3)
    print(f"Does {item3} exist in {list3}? {result3}")