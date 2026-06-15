def check_membership(data_list, item):
    if isinstance(data_list, (list, tuple, set)):
        return item in data_list
    else:
        for element in data_list:
            if element == item:
                return True
        return False
data1 = [1, 5, 10, 15, 20]
data2 = [1, 5, 10, 15, 20]
data3 = [1, 5, 10, 15, 20]
item_to_find_in_data1 = 10
item_to_find_in_data2 = 25
item_to_find_in_data3 = 1
result1 = check_membership(data1, item_to_find_in_data1)
result2 = check_membership(data2, item_to_find_in_data2)
result3 = check_membership(data3, item_to_find_in_data3)
print(f"Data 1: {item_to_find_in_data1} in list? {result1}")
print(f"Data 2: {item_to_find_in_data2} in list? {result2}")
print(f"Data 3: {item_to_find_in_data3} in list? {result3}")
print("\n--- Comparison with 'in' operator ---")
print(f"Data 1: {item_to_find_in_data1} in data1? {item_to_find_in_data1 in data1}")
print(f"Data 2: {item_to_find_in_data2} in data2? {item_to_find_in_data2 in data2}")
print(f"Data 3: {item_to_find_in_data3} in data3? {item_to_find_in_data3 in data3}")
if __name__ == '__main__':
    pass