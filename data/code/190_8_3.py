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
    print("Comparison using Manual Loop:")
    print(f"Manual check for {item_present} in {list1}: {manual_loop_check(list1, item_present)}")
    print(f"Manual check for {item_absent} in {list1}: {manual_loop_check(list1, item_absent)}")
    print("-" * 20)
    print("Most Efficient Implementation using 'in' operator:")
    print(f"Result for {item_present} in {list1}: {check_membership(list1, item_present)}")
    print(f"Result for {item_absent} in {list1}: {check_membership(list1, item_absent)}")
    large_list_test = list(range(100000))
    large_item_present = 50000
    large_item_absent = 100001
    import time
    start_time = time.perf_counter()
    result_builtin = large_item_present in large_list_test
    end_time = time.perf_counter()
    print(f"\nPerformance test on list of size 100,000:")
    print(f"Built-in 'in' operator check for {large_item_present}: {result_builtin}")
    print(f"Time taken: {(end_time - start_time) * 1e6:.3f} microseconds")
    start_time = time.perf_counter()
    result_loop = manual_loop_check(large_list_test, large_item_present)
    end_time = time.perf_counter()
    print(f"Manual loop check for {large_item_present}: {result_loop}")
    print(f"Time taken: {(end_time - start_time) * 1e6:.3f} microseconds")