def check_item_exists(item, data_list):
    if not isinstance(data_list, list):
        raise ValueError("The second argument must be a list.")
    
    return item in data_list

if __name__ == '__main__':
    try:
        list1 = [1, 2, 3, 4, 5]
        item1 = 3
        result1 = check_item_exists(item1, list1)
        print(f"Does {item1} exist in {list1}? {result1}")
        
        list2 = ['apple', 'banana', 'cherry']
        item2 = 'apple'
        result2 = check_item_exists(item2, list2)
        print(f"Does {item2} exist in {list2}? {result2}")
        
        list3 = [10, 20, 30]
        item3 = 5
        result3 = check_item_exists(item3, list3)
        print(f"Does {item3} exist in {list3}? {result3}")
        
        list4 = []
        item4 = 1
        result4 = check_item_exists(item4, list4)
        print(f"Does {item4} exist in {list4}? {result4}")
    except ValueError as e:
        print(e)