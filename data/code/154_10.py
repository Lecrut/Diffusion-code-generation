def count_list_items(data_list):
    return len(data_list)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b', 'c']
    empty_list = []
    count1 = count_list_items(list1)
    count2 = count_list_items(list2)
    count_empty = count_list_items(empty_list)
    print(f"The number of items in {list1} is: {count1}")
    print(f"The number of items in {list2} is: {count2}")
    print(f"The number of items in {empty_list} is: {count_empty}")