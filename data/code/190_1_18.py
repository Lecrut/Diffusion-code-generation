def check_item_presence(target_list, item):
    return item in target_list

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    item1 = 'banana'
    result1 = check_item_presence(sample_list, item1)
    print(f"Does '{item1}' exist in the list? {result1}")
    
    item2 = 'grape'
    result2 = check_item_presence(sample_list, item2)
    print(f"Does '{item2}' exist in the list? {result2}")
    
    item3 = 'apple'
    result3 = check_item_presence(sample_list, item3)
    print(f"Does '{item3}' exist in the list? {result3}")