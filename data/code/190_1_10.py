def check_item_presence(data_list, target):
    return target in data_list

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    target_string1 = "banana"
    result1 = check_item_presence(sample_strings, target_string1)
    print(f"Does '{target_string1}' exist in the list? {result1}")
    
    target_string2 = "grape"
    result2 = check_item_presence(sample_strings, target_string2)
    print(f"Does '{target_string2}' exist in the list? {result2}")
    
    empty_list = []
    target_string3 = "orange"
    result3 = check_item_presence(empty_list, target_string3)
    print(f"Does '{target_string3}' exist in an empty list? {result3}")