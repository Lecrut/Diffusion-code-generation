def check_item_presence(data, item):
    return item in data

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    target1 = 'banana'
    result1 = check_item_presence(sample_list, target1)
    print(f"Does '{target1}' exist in the list? {result1}")
    
    target2 = 'orange'
    result2 = check_item_presence(sample_list, target2)
    print(f"Does '{target2}' exist in the list? {result2}")