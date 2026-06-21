def check_item_exists(item, data_list):
    return item in data_list

if __name__ == '__main__':
    list1 = [10, 20, 30, 40, 50]
    item1 = 30
    result1 = check_item_exists(item1, list1)
    print(f"Does {item1} exist in {list1}? {result1}")
    
    list2 = ['red', 'green', 'blue']
    item2 = 'yellow'
    result2 = check_item_exists(item2, list2)
    print(f"Does {item2} exist in {list2}? {result2}")