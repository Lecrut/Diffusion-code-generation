def check_membership_list(data_list, item):
    return item in data_list
if __name__ == '__main__':
    list1 = [1, 5, 10, 15, 20]
    item1 = 15
    print(f"List: {list1}, Item: {item1}")
    print(f"'in' operator result: {item1 in list1}")
    list2 = ['a', 'b', 'c', 'd']
    item2 = 'c'
    print(f"\nList: {list2}, Item: {item2}")
    print(f"'in' operator result: {item2 in list2}")
    def manual_check(data_list, item):
        for element in data_list:
            if element == item:
                return True
        return False
    print("\n--- Manual Loop Comparison ---")
    print(f"List: {list1}, Item: {item1}")
    print(f"Manual loop result: {manual_check(list1, item1)}")
    list3 = [100, 200, 300]
    item3 = 500
    print(f"\nList: {list3}, Item: {item3}")
    print(f"Manual loop result: {manual_check(list3, item3)}")