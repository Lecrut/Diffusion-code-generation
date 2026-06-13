def check_list_item(data_list, item):
    return item in data_list
if __name__ == '__main__':
    my_list = [1, 5, 8, 10, 3]
    item1 = 8
    item2 = 9
    result1 = check_list_item(my_list, item1)
    print(f"Is {item1} in {my_list}? {result1}")
    result2 = check_list_item(my_list, item2)
    print(f"Is {item2} in {my_list}? {result2}")