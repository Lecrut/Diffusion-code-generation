def check_item_presence(data, item):
    return item in data

if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    item1 = 5
    result1 = check_item_presence(sample_list, item1)
    print(f"Does {item1} exist in the list? {result1}")
    
    item2 = 9
    result2 = check_item_presence(sample_list, item2)
    print(f"Does {item2} exist in the list? {result2}")
    
    item3 = 2
    result3 = check_item_presence(sample_list, item3)
    print(f"Does {item3} exist in the list? {result3}")