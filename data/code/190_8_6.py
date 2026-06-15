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
    def manual_loop_check(data_list, item):
        for element in data_list:
            if element == item:
                return True
        return False
    print("\n--- Comparison ---")
    print(f"Manual loop check for {item_present} in {list1}: {manual_loop_check(list1, item_present)}")
    print(f"Manual loop check for {item_absent} in {list1}: {manual_loop_check(list1, item_absent)}")
    large_list_test = list(range(100000))
    item_to_find = 99999
    import time
    start_time = time.perf_counter()
    result_builtin = item_to_find in large_list_test
    end_time = time.perf_counter()
    start_time = time.perf_counter()
    result_loop = manual_loop_check(large_list_test, item_to_find)
    end_time = time.perf_counter()
    print("\n--- Performance Test (Large List) ---")
    print(f"Built-in 'in' operator result: {result_builtin}")
    print(f"Manual loop result: {result_loop}")
    print(f"Time taken for 'in' operator: {(end_time - start_time) * 1000:.6f} ms")
    print(f"Time taken for manual loop: {(end_time - start_time) * 1000:.6f} ms")