def item_exists_in_list(item, data_list):
    return item in data_list

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    item1 = 3
    print(f"Does {item1} exist in {list1}? {item_exists_in_list(item1, list1)}")
    
    list2 = ['apple', 'banana', 'cherry']
    item2 = 'apple'
    print(f"Does {item2} exist in {list2}? {item_exists_in_list(item2, list2)}")
    
    list3 = [10, 20, 30]
    item3 = 5
    print(f"Does {item3} exist in {list3}? {item_exists_in_list(item3, list3)}")
    
    list4 = []
    item4 = 1
    print(f"Does {item4} exist in {list4}? {item_exists_in_list(item4, list4)}")