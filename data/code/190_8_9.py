def check_membership(data_list, item):
    if isinstance(data_list, (list, tuple, set)):
        return item in data_list
    else:
        try:
            return item in data_list
        except TypeError:
            return False
if __name__ == '__main__':
    list1 = [1, 5, 10, 15, 20]
    list2 = [100, 200, 300, 400]
    large_list = list(range(100000))
    item_present = 15
    item_absent = 99999
    print(f"Checking if {item_present} is in {list1}: {check_membership(list1, item_present)}")
    print(f"Checking if {item_absent} is in {list1}: {check_membership(list1, item_absent)}")
    print("-" * 20)
    def manual_loop_check(data_list, item):
        for element in data_list:
            if element == item:
                return True
        return False
    print("Comparison using 'in' operator:")
    print(f"List1 check (in): {item_present in list1}")
    print(f"Large List check (in): {item_present in large_list}")
    print("\nComparison using Manual Loop:")
    print(f"List1 check (loop): {manual_loop_check(list1, item_present)}")
    print(f"Large List check (loop): {manual_loop_check(large_list, item_present)}")